import threading

import time

import random

N = 8

buffer = N * [None]

free = threading.Semaphore(N)
items = threading.Semaphore(0)

def prod():

    n = 0
    i = 0
    while True:
        time.sleep(random.random())
        free.acquire()
        buffer[i] = n
        i = (i + 1) % N
        n += 1
        items.release()

def cons():
    i = 0
    while True:
        time.sleep(random.random())
        items.acquire()
        print(buffer[i])
        i = (i + 1) % N
        free.release()

def main():

    p = threading.Thread(target=prod, args=[])
    c = threading.Thread(target=cons, args=[])
    p.start()
    c.start()
    p.join()
    c.join()

main()
