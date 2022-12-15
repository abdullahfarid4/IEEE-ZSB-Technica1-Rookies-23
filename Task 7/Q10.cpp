#include <iostream>
#include <string>
#include<bits/stdc++.h>


using namespace std;

int toggle(int n)
{
    if(n == 1) return 0;
    if(n == 0) return 1;
}

int main()
{
    int arr[3][3];
    int arr2[3][3] = { {1,1,1}, {1,1,1}, {1,1,1} };
    for(int i = 0 ; i < 3 ; i++)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            cin >> arr[i][j];
            if(arr[i][j] % 2 != 0)
            {
                arr2[i][j] = toggle(arr2[i][j]);
                if(i <= 1) arr2[i + 1][j] = toggle(arr2[i + 1][j]);
                if(j <= 1) arr2[i][j + 1]  = toggle(arr2[i][j + 1]);
                if (i >= 1) arr2[i - 1][j] = toggle(arr2[i - 1][j]);
                if (j >= 1 ) arr2[i][j - 1] = toggle(arr2[i][j - 1]);
            }
        }
    }
    for(int i = 0 ; i < 3 ; i++)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            cout << arr2[i][j];
        }
        cout << endl;
    }
}


