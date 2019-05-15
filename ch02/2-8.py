import threading
import time

global_variable = 0

semaphore = threading.Semaphore()


def consumer():
    semaphore.acquire()
    global global_variable
    print("consumer variable", global_variable)


def producer():
    global global_variable
    time.sleep(10)
    global_variable += 10
    print("produce variable", global_variable)
    semaphore.release()


for i in range(5):
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
