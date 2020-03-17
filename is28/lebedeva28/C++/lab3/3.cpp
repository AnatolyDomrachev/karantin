#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//номер дня в годy
	cout << "Введите число ";
	cin >> x;
	x=fmod(x,7);
	if (x == 0)
		cout << "7" << endl;
	else 
		cout << x << endl;
	return 0;
}