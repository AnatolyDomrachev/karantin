#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
//является ли число палиндромом
	int x, x1, x2;
	cout << "x = ";
	cin >> x;
	x1=x/100;
	x2=x%10;
	if (x1 == x2)
		cout << "Палиндром" << endl;
	else 
		cout << "Не является палиндромом" << endl;
	return 0;
}
