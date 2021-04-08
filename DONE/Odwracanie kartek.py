# https://adjule.pl/groups/ogolny/problems/031
# solution by Paweł Lewicki

if __name__ == '__main__':
    x = int(input())

    for d in range(0, x):
        string = ""

        n = int(input())

        table = input().split()

        string = ''.join([str(elem) for elem in table])

        compare1 = '0' * n
        compare2 = '1' * n
        compare3 = '1' + '0' * (n - 1)
        compare4 = '0' + '1' * (n - 1)

        if string == compare1:
            print(0)
        elif string == compare2:
            print(1)
        elif string == compare3:
            print(2)
        elif string == compare4:
            print(1)
        else:
            print("NIGDY")
