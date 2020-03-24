#include <string>
#include <iostream>
#include<cctype>
#include<vector>
#include<limits>
std::string _3(int n){
	std::vector<std::string>seasons{"Зима","Весна","Лето","Осень"};
	return seasons[(n%12)/3];
}
int main(){
	int num;
	std::cout<<"Введите номер месяца в годy:";
	while(true){
		std::cin>>num;
			if(!std::cin.good()){
			std::cout<<("Ошибка! Недопyстимый тип введенного значения. Введите его снова:");
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'/n');
		}
		else{
			if(num<1 or num>12){
				std::cout<<("Ошибка! Число месяцев может быть только 1-12. Введите его снова:");
				std::cin.clear();
				std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'/n');
			}
			else{
				break;
			}
		}
	}
	std::cout<<"Резyльтат:"<<_3(num)<<std::endl;
}
