//https://adjule.pl/groups/ogolny/problems/apr2
//solution by Paweł Lewicki

#include <iostream>

using namespace std;

int main() {
    int size = 0;
    int a = 0;
    int x = 0;
    int y = 0;

    int n = 0;
    cin >>n;

    for (int k=0; k<n; k++) {
        size = 0;

        cin >> size;
        int tab[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                cin >> a;
                tab[i][j] = a;
            }
        }

        x=0;
        y=0;
        while (x<size)
        {
            if (tab[x][y] == 0)
                y++;
            else
                x++;
        }
        cout << y+1 << endl;
    }

    return 0;
}
