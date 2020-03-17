#include <string>
#include <iostream>

using namespace std;

int main()
{ 
	int b, i, g, j, n;
	cout << "Введите количество элементов n в массиве: " << endl;
	cin >> n;
	float a[n];
//Напишите программу, которая проверяет, есть ли во введенном массиве одинаковые элементы.
	cout << "Введите массив из " << n << " чисел: " << endl;
	for (i=0; i < n; i++)
		cin >> a[i];
	for	(j=0; j < (n-1); i++)
		for (g=0; g > (j+1) && g < n; g++)
			if (a[j] == a[g])
			{
					cout << "Есть одинаковые элементы в массиве" << endl;
					exit(0);
			}
	cout << "Нет одинаковых элементов в массиве" << endl;
	return 0;
}



