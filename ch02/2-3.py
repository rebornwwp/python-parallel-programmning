import threading


def function(i):
    print("function is running in threading {}".format(i))
    return


threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i, ))
    threads.append(t)
    t.start()
    t.join()
