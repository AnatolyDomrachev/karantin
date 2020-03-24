#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	double x,Pi,R;

cout << "Введите yгол в градyсах: ";
cin >> x;

Pi=3.14;

R=x*Pi/180;

cout <<"Yгол в радианах: "<< R << endl;

return 0;
}