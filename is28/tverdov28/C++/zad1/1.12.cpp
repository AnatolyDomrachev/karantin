#include <iostream>

using namespace std;

int main()
{
    int a=0, b=0, c=1;
    cout << "Введите конечное число\n> ";
    cin >> a;
    //cout << 0;
    while (b<=a)
    {
        cout << b << ' ';
        c ^= b ^= c ^= b;
        c += b;
    }
    return 0;


}
