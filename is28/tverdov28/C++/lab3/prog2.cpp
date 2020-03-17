#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float y, x, z;
//Вывод сyммы цифр в числе
	cout << "Число: ";
	cin >> x;
	y = fmod(x,10);
	x = int(x / 10);
	z = fmod(x, 10);
	x = int(x / 10);
	x = fmod(x, 10);
	x = x + y + z;
	cout << "Сyмма цифр в числе: " << x << endl;
	return 0;
}



