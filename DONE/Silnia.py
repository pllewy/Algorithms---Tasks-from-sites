# https://szkopul.edu.pl/problemset/problem/_X8vz1GyYV67RyrXmXq-_NMW/site/?key=statement
# solution by Paweł Lewicki

if __name__ == '__main__':
    n = int(input())
    result = 1

    for i in range(2, n + 1):
        result *= i
        result %= 10

    print(result)
