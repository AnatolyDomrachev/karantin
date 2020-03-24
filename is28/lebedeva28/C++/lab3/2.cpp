#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x, y, z, c, s;
	cout << "Введите число ";
	cin >> x;
	y=fmod(x,10);
	x=int(x/10);
	z=fmod(x,10);
	x=int(x/10);
	c=fmod(x,10);
	s=y+z+c;	
	

	cout << "сyмма числа " << s << endl;
	return 0;
}