#include <string>
#include <iostream>
#include <math.h>
#include <cmath>

using namespace std;

int main()
{
	float x1, x2, y1, y2, s;
//Нyжно найти расстояние междy точками
	cout << "x1: ";
	cin >> x1;
	cout << "y1: ";
	cin >> y1;
	cout << "x2: ";
	cin >> x2;
	cout << "y2: ";
	cin >> y2;
	s = ((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2));
	s = sqrt(s);
	cout << "Расстояние междy точками равно " << round(s*1000)/1000 << endl;
	return 0;
}



