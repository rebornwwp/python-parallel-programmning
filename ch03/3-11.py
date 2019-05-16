import time

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
time.sleep(10)
print("hello world from process ", rank)
