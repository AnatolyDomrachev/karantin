#include <string>
#include <iostream>

using namespace std;

int main()
{
	string name;
	int age;
	cout << "Как вас зовyт?";

	cin >> name;
	cout << "Привет, " << name;
		
	cout << "Сколько вам лет?";
	cin >> age;
	cout << "Через 10 лет вам бyдет " << age+10 << endl;
	return 0;
}
