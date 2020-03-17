#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
short a,i;
cin >> a;
while (i<a){
	i=i+4;
	}
while (i==a){
	cout << "TRUE" << endl;
	break;
	}
while (i!=a){
	cout << "FALSE" << endl;
	break;
	}
return 0;
}