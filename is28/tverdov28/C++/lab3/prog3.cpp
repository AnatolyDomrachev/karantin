#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//Делится ли число на 7, если да, то вывод 7, иначе вывод остатка
	cout << "Число: ";
	cin >> x;
	x = fmod(x, 7);
	if (x == 0)
		cout << 7 << endl;
  	else 
		cout << x << endl;
	return 0;
}



