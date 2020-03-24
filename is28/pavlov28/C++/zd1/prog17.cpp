#include <string>
#include <iostream>

using namespace std;

int main()
{ 
	string a, b;
	int i;
//Определить, является ли заданное натуральное число палиндромом, 
//то есть таким, запись которого в десятичной системе счисления читается 
//одинаково слева направо и справа налево.
	cout << "Введите натyральное число: " << endl;
	cin >> a;
	for (i=0; a.length()>i; i++)
		b = a[i] + b;
	if (a == b)
		cout << "Палиндром" << endl;
	else 
		cout << "Не палиндром" << endl;
	return 0;
}
