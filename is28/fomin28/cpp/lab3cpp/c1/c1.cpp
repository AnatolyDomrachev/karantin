#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   float x,y,z;
	cout << "введите дробь ";
	cin >> x;
	y = fmod(x,1);
	z = (x - y);
	cout << "Целая часть = " << z << endl;
	cout << "Дроьная часть = " << y << endl;
	return 0;
}
