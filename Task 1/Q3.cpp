#include <iostream>
#include <string>

using namespace std;

int suming(int arr[], int n)
{
    int sum1 = 0;

  if( n < 0) return 0;
  else{
    sum1 = arr[n] + suming(arr, n - 1);
    return sum1;
  }
}

int main()
{
    int n;
    int sum = 0;
    int sum2 = 0;
    cin >> n;
    int m = n;
    int arr[n];
    for(int i = 0 ; i < n ; ++i)
    {
        cin >> arr[i];
        sum += arr[i];
    }
    cout << sum << endl;
    while(m--){
        sum2 += arr[m];
    }
    cout << sum2 << endl;
    cout << suming(arr, n-1);
    return 0;
}
