# https://acm.timus.ru/problem.aspx?space=1&num=1409
# solution by Paweł Lewicki

if __name__ == '__main__':
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    sum = x + y - 1

    print(sum - x, sum - y)