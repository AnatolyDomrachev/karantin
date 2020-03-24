#include <string>
#include <iostream>

using namespace std;

int main()
{
	int n, b, c, b1;
//Напишите программу, печатающую таблицу чисел Фибоначчи, номера которых не превышают заданного значения n.
	cout << "Конечное число Фибоначчи: ";
	cin >> n;
	b = c = 1;
	cout << 0 << endl;
	while (b <= n) 
		{
		cout << b << endl;
		b1 = b;
		b = c;
		c = b1 + c;
		}
	return 0;
}





