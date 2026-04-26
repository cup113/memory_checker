# Memory Checker

A lightweight Windows system tray utility that displays real-time memory usage.

## Features

- Dynamic tray icon showing memory percentage (0-100)
- Color-coded indicators: Green (<70%), Yellow (70-80%), Orange (80-85%), Red (>85%)
- Top 5 memory-consuming processes in the context menu
- Auto-refreshes every 3 seconds

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
