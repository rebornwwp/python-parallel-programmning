from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = list(range(10))
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process = {} recvbuf = {}".format(rank, recvbuf))
