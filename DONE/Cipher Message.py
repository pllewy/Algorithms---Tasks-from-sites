# https://acm.timus.ru/problem.aspx?space=1&num=1654
# solution by Paweł Lewicki

x = input()

stack = [""]
compare = ""

for i in range(0, len(x)):
    compare = stack[-1]
    if x[i] == compare:
        stack.pop()
    else:
        stack.append(x[i])

print(''.join(stack))

# wwstdaadierfflitzzz