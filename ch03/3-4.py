import multiprocessing
import time


def foo():
    time.sleep(0.1)


p = multiprocessing.Process(target=foo)
p.start()
print("process running: ", p, p.is_alive())
p.terminate()
print("process running: ", p, p.is_alive())
p.join()
print("process running: ", p, p.is_alive())
print("process exit code:", p.exitcode)
