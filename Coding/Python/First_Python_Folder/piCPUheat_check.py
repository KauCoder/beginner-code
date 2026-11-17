import os
import shutil
import time

print("Raspberry Pi Monitor Started! Press Ctrl+C to stop.")
print("-" * 50)

try:
    while True:
        # 1. Get CPU temperature (Raspberry Pi specific file path)
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp_raw = int(f.read())
                cpu_temp = temp_raw / 1000.0
        except FileNotFoundError:
            cpu_temp = "N/A (Not on a Raspberry Pi)"

        # 2. Get Disk Space usage
        total, used, free = shutil.disk_usage("/")
        disk_used_pct = (used / total) * 100

        # 3. Print the live dashboard update
        # \r keeps resetting the terminal line so it doesn't spam your screen
        print(f"🌡️ CPU Temp: {cpu_temp}°C  |  💾 Disk Used: {disk_used_pct:.1f}%", end="\r")
        
        # 4. Wait a little before updating
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\nMonitor turned off.")