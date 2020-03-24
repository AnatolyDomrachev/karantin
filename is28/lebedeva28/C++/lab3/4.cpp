#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//число делится на 4 без остатка
	cout << "Введите число ";
	cin >> x;
	x=fmod(x,4);
	if (x == 0)
		cout << true << endl;
	else 
		cout << false << endl;
	return 0;
}