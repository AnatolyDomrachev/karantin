#include <string>
#include <iostream>
#include<cmath>
std::string _4(int n)
{	return n%4==0?"TRUE":"FALSE";	}
int main()
{
	int num;
	std::cout<<"Введите номер дня в годy:";
	std::cin>>num;
	std::cout<<"Резyльтат:"<<_4(num)<<std::endl;
	
}
