#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int S;

cout << "Введите трехзначное число: ";
cin >> S;

std::cout<<std::boolalpha<<not bool(S%4)<<std::endl;

return 0;
}