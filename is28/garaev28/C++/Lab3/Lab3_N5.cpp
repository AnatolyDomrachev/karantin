#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
short day,nedelya;
cin >> day;
nedelya = fmod((day-fmod(day,7)),7);
cout << nedelya << endl;
return 0;
}