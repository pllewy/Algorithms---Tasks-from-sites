# solution

d = int(input())

for p in range(0, d):
    n, m, t = input().split()
    n, m, t = int(n), int(m), int(t)

    cave = [[int(0) for col in range(n+2)] for row in range(m+2)]
    cave2 = [list(x) for x in cave]

    for k in range(0, t):
        x, y = input().split()
        x, y = int(x), int(y)

        cave[x][y] += 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cave2[i][j] = max(cave[i][j], cave[i - 1][j], cave[i + 1][j], cave[i][j - 1], cave[i][j + 1])
        cave = [list(x) for x in cave2]

    print(int(max(max(cave))))
