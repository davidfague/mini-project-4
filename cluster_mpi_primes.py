from mpi4py import MPI
import math, time

def local_sieve(n, start, step):
    segment = [True]*(n+1)
    for p in range(2, int(math.sqrt(n))+1):
        if segment[p]:
            for multiple in range(p*p, n+1, p):
                segment[multiple] = False
    # keep only those congruent to start mod step
    return [i for i in range(start, n+1, step) if segment[i]]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 100000000
step = size
start = 2 + rank

t0 = time.time()
local_primes = local_sieve(N, start, step)
all_primes = comm.gather(len(local_primes), root=0)
if rank == 0:
    total = sum(all_primes)
    print("Total primes:", total)
    print("Elapsed (s):", time.time() - t0)

# example call: mpirun -np 16 python3 cluster_mpi_primes.py