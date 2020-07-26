import time as t
import datetime as dt

sec = int(input("How many seconds?: "))

with open("logs.txt", "w") as f:
    for i in range(sec):
        t.sleep(1)
        now = dt.datetime.now()
        to_write = str(i) + " | " + str(now.day) + " " + t.strftime("%b", t.localtime()) + " " + str(now.year) + " | " \
                   + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " | " \
                   + str(int(now.timestamp())) + "\n"
        f.write(to_write)