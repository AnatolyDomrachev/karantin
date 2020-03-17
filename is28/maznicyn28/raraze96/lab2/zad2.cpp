#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
int x,x1,y,y1;
double l,k1,k2;
cout << "введите координаты точек" << endl;
cin >> x >> y >> x1 >> y1;
k1 = x - x1;
k2 = y - y1;
l = sqrt(k1*k1+k2*k2);
cout << fixed << setprecision(3) << l<< endl;
return 0;
}