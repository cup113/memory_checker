# Memory Checker

[![Python](https://img.shields.io/badge/python-3.12-blue)]()
[![License](https://img.shields.io/github/license/cup113/memory_checker)](LICENSE)
[![Release](https://img.shields.io/github/v/release/cup113/memory_checker)](https://github.com/cup113/memory_checker/releases)
[![Last Commit](https://img.shields.io/github/last-commit/cup113/memory_checker)](https://github.com/cup113/memory_checker/commits)
[![Platform](https://img.shields.io/badge/platform-Windows-blue)]()

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
