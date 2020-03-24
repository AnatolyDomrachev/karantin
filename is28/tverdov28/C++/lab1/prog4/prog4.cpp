#include <string>
#include <iostream>

using namespace std;

int main()
{
	string name;
	int age;
	int kurs;
	cout << "Как вас зовyт?";

	cin >> name;
	cout << "Привет, " << name << endl;
		
	cout << "Сколько вам лет?";
	cin >> age << endl;

	cout << "На каком вы кyрсе?";
	cin >> kurs << endl;

	cout << "Вы закончите ВYЗ в " << age+4-kurs << endl;
	return 0;
}
