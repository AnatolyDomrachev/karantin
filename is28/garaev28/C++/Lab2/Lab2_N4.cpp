#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;
int main()
{
double a, sina, cosa;
cin >> a;
a = a*3.14159265/180;
sina = sin(a);
cosa = cos(a);
cout << fixed << setprecision(3) << sina << " " << cosa << endl;
return 0;
}