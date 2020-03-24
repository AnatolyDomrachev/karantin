#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
double a,aceloe,adrob;
cin >> a;
aceloe = fmod(a,1);
adrob = a - aceloe;
cout << fixed << setprecision(2) << aceloe << "  " << adrob << endl;
return 0;
}