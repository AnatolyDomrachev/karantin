#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
short a,summ;
cin >> a;
while (a>0){
	summ=summ+fmod(a,10);
	a=(a-fmod(a,10))/10;
	}
cout << summ << endl;
return 0;
}