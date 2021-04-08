# https://adjule.pl/groups/ogolny/problems/033
# solution by Paweł Lewicki
import math

if __name__ == '__main__':
    x = int(input())

    for i in range(0, x):
        alpha, beta = input().split()

        print(math.floor((180 - (2 * float(beta))) / float(alpha)))