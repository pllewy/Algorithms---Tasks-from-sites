n, m = input(). split(' ')
n, m = int(n), int(m)
Graph = []
Cost = []

# Macierz incydencji
for i in range(0, n+1):
    sub = []
    for j in range(0, n+1):
        sub.append(int(0))
    Graph.append(sub)

# uzupełnianie macierzy danymi
for i in range(0, m):
    x, y, c = input().split()
    x, y = int(x), int(y)
    Graph[x][y] = int(c)
print(Graph)

# Algorytm
Cost.append([1,0])
acc = Cost.pop()

for i in In:
    if i[0] == acc[0] and i[2] != acc[1]:
        Cost.append()
        Graph[[i[1],acc[1]]] = Graph[acc]+1
    elif i[1] == acc[0] and i[2] != acc[1]:
        Cost.append()





print(Graph)
