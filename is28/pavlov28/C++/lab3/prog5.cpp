#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//Определяется верхняя или нижняя неделя по номерy дня в годy
	cout << "Число: ";
	cin >> x;
	x = bool((fmod(x, 14) <= 7) and (fmod(x, 14) != 0));
	if (x == 1)
		cout << "Верхняя неделя" << endl;
	else
		cout << "Нижняя неделя" << endl;
	return 0;
}

