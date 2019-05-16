from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data {} to process {}".format(data, destination_process))

if rank == 1:
    data = "hello"
    destination_process = 8
    comm.send(data, dest=destination_process)
    print("sending data {} to process {}".format(data, destination_process))

if rank == 4:
    data = comm.recv(source=0)
    print("data received is = {}".format(data))

if rank == 8:
    data = comm.recv(source=1)
    print("data received is = {}".format(data))
