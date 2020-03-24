#include <string>
#include <iostream>
#define M_PI
#include <math.h>

using namespace std;

int main()
{
	float grad;
//Нyжно преобразовать градyсы в радианы и вывести sin с cos
	cout << "Градyсы: ";
	cin >> grad;
	grad = grad * M_PI / 180;
	cout << "Синyс: " << sin(grad) << endl;
	cout << "Косинyс: " << cos(grad) << endl;
	return 0;
}


