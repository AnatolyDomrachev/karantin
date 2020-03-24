#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x, y, z;
	cout << "x= ";
	cin >> x;
	y=floor(x);
	z=fmod(x,1);	
	

	cout << "целая часть " << y << endl;
	cout << "дробная часть" << z << endl;
	return 0;
}
