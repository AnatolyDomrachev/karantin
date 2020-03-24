#include <string>
#include <iostream>

using namespace std;

int main()
{
    int a;
    cout << "Введите возраст ";
    cin >> a;
    if (a%10==1)
        cout << a << " год" << endl;
    if (a%10==2 || a%10==3 && a%100 || a%10==4)
        cout << a << " года" << endl;
    return 0;
}
