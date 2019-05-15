import threading

variable_with_lock = 0
variable_without_lock = 0
COUNT = 10000
lock = threading.Lock()


def inc():
    global variable_with_lock
    for _ in range(COUNT):
        lock.acquire()
        variable_with_lock += 1
        lock.release()


def dec():
    global variable_with_lock
    for _ in range(COUNT):
        lock.acquire()
        variable_with_lock -= 1
        lock.release()


def inc_no():
    global variable_without_lock
    for _ in range(COUNT):
        variable_without_lock += 1


def dec_no():
    global variable_without_lock
    for _ in range(COUNT):
        variable_without_lock -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=inc)
    t2 = threading.Thread(target=dec)
    t3 = threading.Thread(target=inc_no)
    t4 = threading.Thread(target=dec_no)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(variable_with_lock)
    print(variable_without_lock)
