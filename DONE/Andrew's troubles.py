# https://codeforces.com/problemsets/acmsguru/problem/99999/276
# solution by Paweł Lewicki

if __name__ == '__main__':
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    late = y - x
    latemin = int(late / 60)

    if late <= 0:
        print('0')
    elif latemin < 5:
        print('1')
    elif latemin < 15:
        print('2')
    elif latemin < 30:
        print('3')
    else:
        print('4')
