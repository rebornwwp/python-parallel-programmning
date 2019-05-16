import multiprocessing


def foo(i):
    print("call function in process : {}".format(i))
    return


processes = []

for i in range(5):
    p = multiprocessing.Process(target=foo, args=(i,))
    processes.append(p)
    p.start()
    p.join()
