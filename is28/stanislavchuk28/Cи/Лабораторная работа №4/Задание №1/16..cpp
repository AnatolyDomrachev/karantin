#include <string>
#include <iostream>
#include<cctype>
#include<vector>
#include<limits>
void _16(int n){
	bool isprime;
	for(int i=2; i<=n; i++){
	isprime = true;
		for (int j=2; j<=1/2; j++){
			if(i%j==0){
				isprime=false;
					break;
			}
		}
		if(isprime)std::cout<<i<<" ";
	}
	std::cout<<std::endl;
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
	std::cout<<"Резyльтат:";
	_16(num);
}
