# Memory Checker

A lightweight Windows system tray utility that displays real-time memory usage.

## Features

- Dynamic tray icon with color-coded percentage and arc progress ring
- Color-coded indicators: ≤60% Green, 60-75% Green→Yellow, 75-85% Yellow→Orange, 85-95% Orange→Red, >95% Red
- Hover tooltip shows memory percentage, used/total GB, and swap usage
- Auto-refreshes every 2 seconds
- Right-click menu: Exit

## Requirements

- Python 3.x
- psutil
- Pillow
- pystray

## Usage

```bash
pip install psutil pillow pystray
python main.pyw
```
