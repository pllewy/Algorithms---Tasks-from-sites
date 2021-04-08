//https://adjule.pl/groups/ogolny/problems/029
//solution by Paweł Lewicki

#include <iostream>

using namespace std;

int main() {
    int size = 0;
    int a = 0;
    int x = 0;
    bool end = false;

    int n = 0;
    cin >>n;

    for (int k=0; k<n; k++) {
        size = 0;
        a=0;
        end = false;

        cin >> size;
        int tab[size][2];

        for(int j=0;j<2;j++)
            for(int i=0;i<size;i++)
                tab[i][j] = 0;

        for (int i = 0; i < size; i++) {
            cin >> a;
            tab[i][0] = a;
            tab[a-1][1] ++;
        }

        while (!end)
        {
            end = true;
            for(int i=0;i<size;i++)
            {
                if (tab[i][1] == 0)
                {
                    x = tab[i][0];
                    tab[x-1][1]--;
                    tab[i][0] = -1;
                    tab[i][1] = -1;
                    end=false;
                }

            }

        int count = 0;
        for (int i=0; i<size; i++)
        {
            if (tab[i][1] > 0)
                count++;
        }

        cout<<count<<endl;
    }

    return 0;
}
