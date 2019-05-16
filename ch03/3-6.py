import multiprocessing

import random
import time


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("queue is empty.")
                continue
            item = self.queue.get()
            print("do with item: {}".format(item))
            time.sleep(0.1)


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(100):
            self.queue.put(i)


queue = multiprocessing.Queue()

consumer = Consumer(queue)
producer = Producer(queue)
consumer.start()
producer.start()
consumer.join()
producer.join()
