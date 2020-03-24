#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
double x,b;
int a;
cin >> x;
a = int(x);
b = x - a;
cout << "(" << a << ", " << b << ")";
return 0;
}