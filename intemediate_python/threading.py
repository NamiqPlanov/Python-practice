from threading import Thread,Lock
import time

database_value = 0
def increase():
    global database_value

    local_copy = database_value
    local_copy+=1
    time.sleep(0.1)
    database_value = local_copy



if __name__ =='__main__':
    lock = Lock
    print('start value',database_value)
    thread_1 = Thread(target=increase)
    thread_2 = Thread(target=increase)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print('end_value',database_value)