from __future__ import annotations

import threading
import time

import psutil
import pystray
from PIL import Image, ImageDraw, ImageFont
from pystray import MenuItem as item

VERSION = "1.0.0"


# --- 1. 颜色插值 ---
def interpolate_color(percent: float) -> tuple[int, int, int]:
    """0%绿 -> 60%绿 -> 75%黄 -> 85%橙 -> 95%红 -> 100%红"""
    if percent <= 60:
        return (55, 174, 0)
    elif percent <= 75:
        t = (percent - 60) / 15
        return (int(55 + 119 * t), int(174 - 8 * t), 0)
    elif percent <= 85:
        t = (percent - 75) / 10
        return (174, int(166 - 87 * t), 0)
    elif percent <= 95:
        t = (percent - 85) / 10
        return (174, int(79 - 79 * t), 0)
    else:
        return (174, 0, 0)


# --- 2. 动态图标生成 ---
def generate_icon(percent: float) -> Image.Image:
    w = h = 64
    image = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    color = interpolate_color(percent)

    m = 2
    if hasattr(draw, "rounded_rectangle"):
        draw.rounded_rectangle((m, m, w - m, h - m), radius=8, fill=(*color, 200))
    else:
        draw.rectangle((m, m, w - m, h - m), fill=(*color, 200))

    try:
        font = ImageFont.truetype("arialbd.ttf", 44)
    except IOError:
        font = ImageFont.load_default()
    draw.text((w / 2, h / 2), str(int(percent)), fill="white", anchor="mm", font=font)
    return image


def exit_action(icon: pystray.Icon, _: pystray.MenuItem) -> None:  # pyright: ignore[reportInvalidTypeForm]
    icon.visible = False
    icon.stop()


# --- 3. 后台刷新线程 ---
def update_loop(icon: pystray.Icon) -> None:  # pyright: ignore[reportInvalidTypeForm]
    icon.visible = True
    last_percent = -1
    last_title = ""
    while icon.visible:
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        used_gb = mem.used / 1073741824
        total_gb = mem.total / 1073741824
        title = f"Memory: {mem.percent:.1f}%\nUsed: {used_gb:.1f} GB / {total_gb:.1f} GB"
        if swap.total > 0:
            swap_used_gb = swap.used / 1073741824
            swap_total_gb = swap.total / 1073741824
            title += f"\nSwap: {swap_used_gb:.1f} GB / {swap_total_gb:.1f} GB"

        pct = int(mem.percent)
        if pct != last_percent:
            icon.icon = generate_icon(mem.percent)
            last_percent = pct
        if title != last_title:
            icon.title = title
            last_title = title
        time.sleep(2)


# --- 4. 主入口 ---
def main() -> None:
    initial_percent = psutil.virtual_memory().percent
    icon_image = generate_icon(initial_percent)

    menu = pystray.Menu(
        item(f"Memory Checker v{VERSION}", None, enabled=False),
        item("❌ Exit", exit_action),
    )

    tray_icon = pystray.Icon("MemMonitor", icon_image, f"Memory: {initial_percent}%", menu=menu)

    threading.Thread(target=update_loop, args=(tray_icon,), daemon=True).start()
    tray_icon.run()


if __name__ == "__main__":
    main()
