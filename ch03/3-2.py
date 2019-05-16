import multiprocessing


def foo():
    name = multiprocessing.current_process().name
    print(name)


p = multiprocessing.Process(target=foo, name="foo_process")
p.start()
