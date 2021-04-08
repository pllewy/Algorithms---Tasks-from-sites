size = int(input)
data = int(input()).split()

stack = [0][0][0]
compare = ""
maxlevel = 0

for i in range(0, size):
    maxlevel = 0
    compare = stack[-1][-1][-1]

    if data[2 * i] < compare:
        stack.append(data[2*i], data[2*i+1], [maxlevel])
    else:
        maxlevel = 0
        stack.pop()

    print(stack)

