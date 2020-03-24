#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	double S,A,B;

cout << "Введите число: ";
cin >> S;

A=trunc(S);

B=S-A;

cout <<"Целая часть числа: "<< A << " Дробная часть числа:" << B << endl;

return 0;
}