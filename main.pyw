import time
import threading
import psutil
from PIL import Image, ImageDraw, ImageFont
import pystray
from pystray import MenuItem as item


# --- 1. 动态图标生成 ---
def generate_icon(percent: float) -> Image.Image:
    """根据内存百分比动态生成带有数字和颜色的图标"""
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # 颜色区分
    if percent < 70:
        color = (55, 174, 0)  # Green
    elif percent < 80:
        color = (174, 166, 0)  # yellow
    elif percent < 85:
        color = (174, 79, 0)  # Orange
    else:
        color = (174, 0, 0)  # Red

    try:
        font = ImageFont.truetype("arialbd.ttf", 48)
    except IOError:
        font = ImageFont.load_default()

    text = f"{int(percent)}"
    draw.text((width / 2, height / 2), text, fill=color, anchor="mm", font=font)

    return image


# --- 2. 获取 Top 5 内存占用进程 ---
def get_top_processes():
    """获取当前内存占用最大的5个进程"""
    procs = []
    for p in psutil.process_iter(["name", "memory_percent"]):
        try:
            if p.info["memory_percent"] is not None:
                procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    top_5 = sorted(procs, key=lambda x: x["memory_percent"], reverse=True)[:5]

    menu_items = [item("📊 Top Processes", None, enabled=False)]
    for p in top_5:
        name = p["name"][:15] + "..." if len(p["name"]) > 15 else p["name"]
        mem = p["memory_percent"]
        menu_items.append(item(f"{name} - {mem:.1f}%", lambda: None))

    return menu_items


# --- 3. 更新菜单 ---
def update_menu(icon):
    """更新托盘菜单的进程列表"""
    process_items = get_top_processes()
    process_items.append(pystray.Menu.SEPARATOR)
    process_items.append(item("🔄 Refresh", lambda icon, _: update_menu(icon)))
    process_items.append(pystray.Menu.SEPARATOR)
    process_items.append(item("❌ Exit", exit_action))
    icon.menu = pystray.Menu(*process_items)


def exit_action(icon, _):
    icon.visible = False
    icon.stop()


# --- 4. 后台刷新线程 ---
def update_loop(icon: pystray.Icon):
    icon.visible = True
    while icon.visible:
        mem_percent = psutil.virtual_memory().percent
        icon.icon = generate_icon(mem_percent)
        icon.title = f"Memory: {mem_percent}%"
        time.sleep(3)


# --- 5. 主入口 ---
def main():
    initial_percent = psutil.virtual_memory().percent
    icon_image = generate_icon(initial_percent)

    # 创建初始菜单（不能传函数）
    initial_menu = pystray.Menu(
        item("📊 Loading...", None, enabled=False),
        pystray.Menu.SEPARATOR,
        item("❌ Exit", exit_action),
    )

    tray_icon = pystray.Icon(
        "MemMonitor", icon_image, f"Memory: {initial_percent}%", menu=initial_menu
    )

    # 初始化菜单（加载真实进程列表）
    update_menu(tray_icon)

    # 启动后台更新线程
    threading.Thread(target=update_loop, args=(tray_icon,), daemon=True).start()

    tray_icon.run()


if __name__ == "__main__":
    main()
