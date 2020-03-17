#include <string>
#include <iostream>
#include<cmath>
std::string _5(int n)
{	return (n/7+1)%2==0?"TRUE":"FALSE";	}
int main()
{
	int num;
	std::cout<<"Введите номер дня в годy:";
	std::cin>>num;
	std::cout<<"Резyльтат:"<<_5(num)<<std::endl;
	
}