import psutil
import platform
from datetime import datetime

def show_stats():
    print(f"\n--- System Status | {datetime.now().strftime('%H:%M:%S')} ---")
    print(f"OS     : {platform.system()} {platform.release()}")
    
    # CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU    : {cpu}%")
    
    # RAM
    ram = psutil.virtual_memory()
    used = ram.used / (1024**3)
    total = ram.total / (1024**3)
    print(f"RAM    : {used:.2f}GB / {total:.2f}GB ({ram.percent}%)")

if __name__ == "__main__":
    show_stats()
