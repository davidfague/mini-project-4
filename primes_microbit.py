from microbit import *
import utime

def sieve(n):
    a = bytearray(n+1)
    a[0] = a[1] = 1  # mark non-prime
    for i in range(2, int(n**0.5) + 1):
        if not a[i]:
            for j in range(i*i, n+1, i):
                a[j] = 1
    return [i for i in range(2, n+1) if not a[i]]

# Benchmark
N = 20000
t0 = utime.ticks_ms()                     # start tick
primes = sieve(N)
elapsed = utime.ticks_diff(utime.ticks_ms(), t0)  # safe diff in ms

display.scroll(str(elapsed) + "ms")
print(elapsed)