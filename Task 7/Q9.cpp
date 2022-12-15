#include <iostream>
#include <string>
#include<bits/stdc++.h>


using namespace std;

int main()
{
    int x, y;
    string s;
    bool flag = true;
    int county = 0;
    cin >> x;
    while(flag)
    {
        x++;
        s = to_string(x);
        for(int i = 0 ; i < 4 ; i++)
        {
            char c = s[i];
            y = count(s.begin(), s.end(), c);
            if(y == 1)
            {
                county++;
            }
        }
        if(county == 4)
        {
            cout << x;
            break;
        }
        county = 0;
    }
}


