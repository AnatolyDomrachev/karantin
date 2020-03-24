#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float y, x;
//Вывод целой и дробной части числа
	cout << "Число: ";
	cin >> x;
	y = fmod(x,1);
	x = floor(x);
	cout << "Целое: " << x << endl;
	cout << "Остаток: " << y << endl;
	return 0;
}


