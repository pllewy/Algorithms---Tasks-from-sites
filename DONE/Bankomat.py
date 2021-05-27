nom = [1, 2, 5, 10, 20]

n = int(input())

for q in range(0, n):
    wart = []
    d = []
    k = 0

    d = input().split(' ')
    d = [int(x) for x in d]
    k = d.pop()

    # da się uprościć
    for i in range(0, 3):
        while d[i] > (2 * nom[i+2] // nom[i]):
            d[i] -= nom[i+2]//nom[i]
            d[i+2] += 1

    if k % 10 != 0:
        print('NIE')
    else:
        k = int(k / 10)

        for i in range(0, k + 1):
            wart.append(0)
        wart[0] = 1

        j = 0
        while j < 5 and wart[k] == 0 and nom[j] <= k:
            if 0 < d[j]:
                current = nom[j]
                d[j] -= 1

                for i in range(k, -1, -1):
                    if wart[i] == 1 and i + current < len(wart):
                        wart[i + current] = 1
            else:
                j += 1

    if wart[k] == 1:
        print('TAK')
    else:
        print('NIE')
