#include <string>
#include <iostream>
#include<cctype>
#include<vector>
#include<limits>
int _11(int n){
	if(n<0)return 0;
	if(n==0 or n==1)return 1;
	return _11(n-1) + _11(n-2);
}
int main(){
	int num;
	std::cout<<"Введите число n:";
	while(true){
		std::cin>>num;
			if(!std::cin.good()){
			std::cout<<("Ошибка! Недопyстимый тип введенного значения. Введите его снова:");
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'/n');
		}
		else{
			if(num<2){
				std::cout<<("Ошибка! Число должно быть больше 1. Введите его снова:");
				std::cin.clear();
				std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'/n');
			}
			else{
				break;
			}
		}
	}
	std::cout<<"Резyльтат:"<<_11(num)<<std::endl;
}
