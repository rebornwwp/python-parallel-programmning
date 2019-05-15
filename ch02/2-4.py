import threading


def function():
    print(threading.currentThread().getName())


t1 = threading.Thread(target=function, name="first_threading")
t2 = threading.Thread(target=function, name="second_threading")
t3 = threading.Thread(target=function, name="third_threading")
t4 = threading.Thread(target=function, name="fifth_threading")
t1.start()
t2.start()
t3.start()
t4.start()

t1 = threading.Thread(target=function)
t2 = threading.Thread(target=function)
t3 = threading.Thread(target=function)
t4 = threading.Thread(target=function)
t1.start()
t2.start()
t3.start()
t4.start()
