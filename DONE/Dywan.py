# https://adjule.pl/groups/ogolny/problems/mwpz2014y
# solution by Paweł Lewicki

if __name__ == '__main__':
    count = input();
    for i in range(0,int(count)):
        mylist = input()
        newlist = mylist.split(' ')
        mytuple = tuple(newlist)
        print(int(mytuple[0]) * int(mytuple[1]))