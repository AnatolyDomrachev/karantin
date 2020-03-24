#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//верхняя неделя
	cout << "Введите число ";
	cin >> x;
	x= bool((fmod(x,14) <= 7) and (fmod(x,14) !=0));
	if (x == 1)
		cout << "Верняя неделя" << endl;
	else 
		cout << "Нижняя неделя" << endl;
	return 0;
}