def largest_prime_factor(N):
    currentMax = 0
    if N == 1:
        return 1
    for i in range(1,(N//2)+1):
        if N%i == 0 and isPrime(i):
            currentMax = i if i>currentMax else currentMax
    if currentMax == 1:
        return N
    return currentMax

def isPrime(N):
    for i in range(2,int(N/2)+1):
        if N%i == 0:
            return False
    return True