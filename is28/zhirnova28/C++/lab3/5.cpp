#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int x,y;

cout << "Введите номер дня в годy: ";
cin >> x;

y=(x+1)/7;

std::cout<<std::boolalpha<<bool(y%2==0 or (x%7==0 and y%2==0))<<std::endl;

return 0;
}