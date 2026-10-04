from datetime import datetime
import time

while True:
    now = datetime.now()
    formatted_time = now.strftime("%I:%M:%S %p")  # 12-hour format
    
    print(formatted_time, end="\r")
    time.sleep(1)