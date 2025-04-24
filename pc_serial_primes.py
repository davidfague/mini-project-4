import time

def sieve(n):
    a = [False]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if not a[i]:
            for j in range(i*i, n+1, i):
                a[j] = True
    return [i for i in range(2, n+1) if not a[i]]

if __name__ == "__main__":
    N = 100000000
    t0 = time.time()
    primes = sieve(N)
    print("Found", len(primes), "primes")
    print("Elapsed (s):", time.time() - t0)