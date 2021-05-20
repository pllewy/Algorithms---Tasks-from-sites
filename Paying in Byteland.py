import sys

turns = int(input())

for x in range(0, turns):
    n = int(sys.stdin.readline())

    wynik = 0
    i = 1

    while 1:
        i *= 2
        if n < i:
            break
        wynik += 1

    n = n - (i // 2 - 1)

    while n > 0:
        if n % 2 == 1:
            wynik += 1
        n = n // 2

    print(wynik)
