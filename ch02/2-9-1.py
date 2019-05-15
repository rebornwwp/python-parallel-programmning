from threading import Condition, Thread

current = 'A'
condition = Condition()


class Athread(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'A':
                    condition.wait()
                print('A')
                current = 'B'
                condition.notify_all()


class Bthread(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'B':
                    condition.wait()
                print('B')
                current = 'C'
                condition.notify_all()


class Cthread(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != 'C':
                    condition.wait()
                print('C')
                current = 'A'
                condition.notify_all()


a = Athread()
b = Bthread()
c = Cthread()
a.start()
b.start()
c.start()
a.join()
b.join()
c.join()
