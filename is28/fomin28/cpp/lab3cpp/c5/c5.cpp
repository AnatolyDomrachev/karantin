#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{  float x,y;
	bool z;
	cout << "ввелите номер дня";
	cin >> x;
	y = fmod((x/8),4); 
	z = y==0;
	if (z==0) cout << "false" << endl;
	else cout << "true" << endl;
    return 0;
}
