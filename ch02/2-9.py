import time
from threading import Condition, Thread

items = []
condition = Condition()


class Consumer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()

    def consume(self):
        global items
        global condition
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("items have no data.")
        i = items.pop()
        print("consume data is {}".format(i))
        condition.notify()
        condition.release()


class Producer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(50):
            self.produce(i)

    def produce(self, i):
        global items
        global condition
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("items had full.")
        items.append(i)
        condition.notify()
        condition.release()


t1 = Consumer()
t2 = Producer()
t1.start()
t2.start()
t1.join()
t2.join()
