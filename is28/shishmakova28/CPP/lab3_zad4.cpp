/*print('Введите трехзначное число')
A=int(input())
print(not bool(A%4))*/
#include  <iostream>

using namespace std;

int main()
{
	int den;
	cout << "Введите трехзначное число\n";
	cin >> den;
	std::cout<<std::boolalpha<< not bool(den%4)<<std::endl;
	return 0;
}