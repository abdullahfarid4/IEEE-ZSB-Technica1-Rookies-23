#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    long t;
    //long temp = 86400;
    cin >> n >> t;
    int arr[n];
    for(int i = 0 ; i < n ; i++)
    {
        cin >> arr[i];
    }
    for(int i = 0 ; i < n ; i++)
    {
        t -= (86400 - arr[i]);
        if(t <= 0) {
            cout << (i+1);
            break;
        }
    }
    return 0;
}
