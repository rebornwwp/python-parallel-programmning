import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print(name)


background_p = multiprocessing.Process(name="back_process", target=foo)
background_p.daemon = True
background_p.start()
