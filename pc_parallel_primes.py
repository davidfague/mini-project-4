import time
from multiprocessing import Pool

def mark_multiples(args):
    start, step, n = args
    return [i for i in range(start, n+1, step) if is_prime(i)]

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    N = 100000000
    num_workers = 4
    pool = Pool(num_workers)
    # split the odd numbers among workers
    tasks = [(3 + 2*i, 2*num_workers, N) for i in range(num_workers)]
    t0 = time.time()
    results = pool.map(mark_multiples, tasks)
    pool.close()
    pool.join()
    primes = [2] + [p for sub in results for p in sub]
    print("Found", len(primes), "primes")
    print("Elapsed (s):", time.time() - t0)