import time

start_time = time.time()


def Rozmien(x):
    if len(tab) > x:
        return tab[x]
    else:
        a = x // 2
        b = x // 3
        c = x // 4

        wynik = max(x, Rozmien(a) + Rozmien(b) + Rozmien(c))
        if x == len(tab):
            tab.append(wynik)
        return wynik


tab = []
for i in range(0, 12):
    tab.append(i)


for i in range(12, 50000):
    Rozmien(i)

print("--- %s seconds ---" % (time.time() - start_time))

for i in range(0, 10):
    n = input()
    if n != "":
        n = int(n)
        print(Rozmien(n))
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        break
print(len(tab))
print("--- %s seconds ---" % (time.time() - start_time))
