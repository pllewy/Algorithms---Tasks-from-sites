# https://pl.spoj.com/problems/PRIME_T/
# solution by Paweł Lewicki

import math

if __name__ == '__main__':
    x = int(input())

    for j in range(0, x):
        n = int(input())
        isPrime = 0

        if n == 1:
            isPrime = 1
        elif n == 2:
            isPrime = 0
        else:
            for i in range(2, math.ceil(math.sqrt(n)+1)):
                if n % i == 0:
                    isPrime = 1

        if isPrime == 0:
            print("TAK")
        else:
            print("NIE")
