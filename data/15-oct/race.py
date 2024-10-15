import time
from threading import Thread

value = 0 

def incr():
    global value
    tmp = value
    time.sleep(.001)
    value = tmp + 20

threads = []
for _ in range(10):
    threads.append(Thread(target=incr))

for t in threads:
    t.start()

for t in threads:
    t.join()

print(value)  # always wrong!
