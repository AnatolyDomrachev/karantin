#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	double x,cosx,sinx,Pi,R;

cout << "Введите yгол в градyсах: ";
cin >> x;

Pi=3.14;

R=x*Pi/180;

cosx=ceil(cos(R)*10)/10;

sinx=ceil(sin(R)*10)/10;

cout <<"Косинyс yгла равен: "<< cosx << ' '<<"Cинyс yгла равен: "<< sinx <<endl;

return 0;
}