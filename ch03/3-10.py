import multiprocessing


def function_square(data):
    result = data * data
    return result


inputs = list(range(100))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(function_square, inputs)
pool.close()
pool.join()
print(pool_outputs)
