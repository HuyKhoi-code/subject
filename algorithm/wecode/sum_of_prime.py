def Prime(n):
    sieve = [True] * (n+1)
    primes = []
    for i in range (2, n+1):
        if (sieve[i]):
            primes.append(i)
            for j in range (i, n+1, i):
                sieve[j] = False
    return primes
n = int(input())
check = set()
primes_list = Prime(n)
count = 0
for i in primes_list:
    check.add(i)
    if (n-i in check):
        count += 1
print (count)

