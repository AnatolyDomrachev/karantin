/*print('Введите день недели')
A=int(input())
B=A+1//7
print(not bool(B%2==0 or (A%7==0 and B%2==0)))*/
#include  <iostream>

using namespace std;

int main()
{
	int den,B;
	cout << "Введите день недели\n";
	cin >> den;
	B=den+1/7;
	std::cout<<std::boolalpha<<  bool(B%2==0 or (den%7==0 and B%2==0))<<std::endl;
	return 0;
}