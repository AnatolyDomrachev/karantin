#include <iostream>
#include <math.h>

using namespace std;

int main()
{
double x,si,co;
cout << "введите óгол" << endl;
cin >> x;
x = x * 3.14 / 180;
si = sin(x);
co = cos(x);
cout << "sin =" << si << "cos =" << co << endl;
return 0;
}