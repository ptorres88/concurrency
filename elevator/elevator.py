#time.sleep()
#threading.Thread(target=)
#setDaemon(True)

#start
import threading
import time
import random

N = 20
delay = 1
current = 0
maxfloor = 0
minfloor = N

buffer = [0] * (N + 1)

def request():
    floor = random.randint(1,N)
    buffer[floor] += 1
    while True:
        rest = random.randint(5,10)
        time.sleep(rest)
        floor = random.randint(1,N)
        buffer[floor] += 1

        for i in range(N, current ,-1):
            if buffer[i] > 0:
                maxfloor = i
                break

        for i in range(0, current):
            if buffer[i] > 0:
                minfloor = i
                break

def visualize():
    while True:
        time.sleep(5)
        str = ''
        for i in range(N + 1):
            str += str(buffer[i]) + ' '
        print str

def start():
    up()

def up():
    global current
    j = current
    for i in range(j,maxfloor):
        sleep(1)
        current = i
        if buffer[current] > 0:
            buffer[current] = 0
    down()

def down():
    j = current
    for i in range(current,minfloor,-1):
        sleep(1)
        current = i
        if buffer[current] > 0:
            buffer[current] = 0
    up()

t1 = threading.Thread(target=request)
t2 = threading.Thread(target=start)

t1.start()
t2.start()
