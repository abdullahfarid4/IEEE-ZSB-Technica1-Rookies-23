#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, k;
    int maax = 0;
    int c = 0;
    int c1 = 0;
    cin >> n >> k;
    string arr[n];
    for(int i = 0 ; i < n ; ++i){
        cin >> arr[i];
    }
    for(int i = 0 ; i < n ; i++)
    {
        for(int j = i + 1 ; j < n ; j++)
        {
            c = 0;
            for(int m = 0 ; i < k ; i++)
            {
                if(int(arr[i][m]) + int(arr[j][m]) >= 1)
                {
                    c += 1;
                }
            }
            if(c > maax)
            {
                maax = c;
                c1 = 1;
            }
            if(c == maax)
            {
                c1 += 1;
                continue;
            }
        }
    }
    cout << maax << endl;
    cout << c1;
    return 0;
}
