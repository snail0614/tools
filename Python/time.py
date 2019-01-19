from datetime import datetime
time_str = None
try:
    dev_create_time1 = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").strftime("%Y%m%d%H%M%S")
    dev_create_time2 = datetime.now().strftime("%Y-%m-%d%H%M%S")
    print(dev_create_time1)
    print(dev_create_time2)
except:
    dev_create_time3 = datetime.now().strftime("%Y%m%d%H%M%S")
    print(dev_create_time3)
    dev_create_time2 = datetime.now().strftime("%Y-%m-%d%H%M%S")
    print(dev_create_time2)