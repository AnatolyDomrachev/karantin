#include<iostream> 
#include<vector> 
#include<iterator> 
#include<algorithm> 
#include<iomanip>
main(){
	float temp;
	std::vector<float>vec;
	std::cout<<"Введите элементы массива:"<<std::endl;
	for(int i=0; i<10; i++){
		std::cin>>temp;
		vec.push_back(temp);
		}
	std::cout<<"Массив:"<<std::endl;
	for(auto item:vec){
	std::cout<<item<<" ";
	}
	std::cout<<std::endl;
	std::cout<<"Массив образyет  "<<(std::is_sorted(vec.begin(),vec.end())?"возрастающyю последовательность":"не возрастающyю последовательность")<<std::endl;
}