# Linux System Monitor 🐧

A minimalist, high-performance system resource monitor written in Python. Specifically tested and optimized for Arch-based distributions like **CachyOS**.

## 🚀 Overview
This script provides a clean terminal output for real-time system tracking, ideal for users who prefer lightweight tools over heavy GUI monitors.

## 📊 Monitored Metrics
- **OS Info:** Distribution and kernel release.
- **CPU:** Real-time usage percentage (1s interval).
- **RAM:** Detailed memory consumption (Used vs Total in GB).
- **Uptime:** Current system session time.

## 🛠️ Installation
Ensure you have Python and `psutil` installed on your system:

```bash
sudo pacman -S python-psutil
