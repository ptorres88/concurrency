import threading
import time
import random

N = 8
buffer = N * ['x']
free = threading.Semaphore(N)
items = threading.Semaphore(0)
sem = threading.Semaphore(1)

def prod():
    i = 0
    while True:
        time.sleep(random.random())
        free.acquire()
        i = (i + 1) % N
	buffer[i] = '.'
        items.release()

def cons():
    i = 0
    while True:
        time.sleep(random.random())
        items.acquire()
        i = (i + 1) % N
	buffer[i] = 'x'
        free.release()

def check():
    while True:
        time.sleep(1)
        bufstr = ""
        for k in range(N):
            bufstr += buffer[k] + ' '
        print(bufstr)

def main():
    p = threading.Thread(target=prod, args=[])
    c = threading.Thread(target=cons, args=[])
    y = threading.Thread(target=check, args=[])
    p.start()
    c.start()
    y.start()
    p.join()
    c.join()
    y.join()

main()
