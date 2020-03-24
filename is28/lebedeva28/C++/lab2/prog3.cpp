#include <string>
#include <iostream>
#define M_PI
#include <math.h>

using namespace std;

int main()
{
	float grad;
//Нyжно преобразовать градyсы в радианы
	cout << "Градyсы: ";
	cin >> grad;
	grad = grad * M_PI / 180;
	cout << "Радианы: " << grad << endl;
	return 0;
}
