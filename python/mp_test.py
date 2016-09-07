#!/usr/bin/python env
from multiprocessing import Queue, Process
import random

def worker():
    """Basic worker"""
    nums = [random.randrange(1,101,1) for num in range (4)]
    print("{r1}, {r2}, {r3}, {r4}".format(r1=nums[0], r2=nums[1], r3=nums[2], r4=nums[3]))
    print("{r1} + {r2} + {r3} + {r4} = {r5}".format(r1=nums[0], r2=nums[1], r3=nums[2], r4=nums[3], r5=sum(nums)))
    print('\n')
    return

if __name__ == '__main__':
    tasks = []
    for i in range(5):
        p = Process(target=worker)
        tasks.append(p)
        print("Starting process {}".format(i))
        p.start()
