n = int(input())
length = n + 1
# n + 1 because starts at 0
sieve = [0] * length
for i in range(2,length):
    if sieve[i] == 0:
        # n + 1 because otherwise we don't hit last number
        for j in range(i,length,i):
            sieve[j] = i
            
def isPrime(n):
    return sieve[n] == n

def calculateGoldbach(n):
    for i in range(n-2,-1,-1):
        if isPrime(i):
            return i - (n - i)
    return -1
 
i = 0
while n >= 3:
    n = calculateGoldbach(n)
    i += 1

print(i)