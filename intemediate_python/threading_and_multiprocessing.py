from multiprocessing import Process
import os
import time

def sum_numbers():
    for i in range(5):
        i+=1
        time.sleep(0.01)
processes = []
num_processes = os.cpu_count()
for i in range(num_processes):
    p = Process(target=sum_numbers)
    processes.append(p)
for p in processes:
    p.start()
for p in processes:
    p.join()
print('end task')
