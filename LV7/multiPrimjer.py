from multiprocessing import Process, Queue
import random

import datetime
from local_machine_info import print_machine_info

print("Datum:" , datetime.datetime.now())


print_machine_info()
print("**************************************************")

def rand_num():
    num = random.random()
    print(("\n %f" % num))

if __name__ == '__main__':
    queue = Queue()

    processes = [Process(target=rand_num, args=())]

    for p in processes:
        p.start()

    for p in processes:
        p.join()