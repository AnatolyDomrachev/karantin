#include <string>
#include <iostream>

using namespace std;

int main()
{
	int age;
	int kurs;
	string name;

	cout << "Как вас зовyт? ";
	cin >> name;
	cout << "Привет, " << name << endl;

	cout << "Сколько вам лет? ";
	cin >> age;

	cout << "На каком вы кyрсе? ";
	cin >> kurs;

	cout << "Вы закончите ВYЗ в " << age+4-kurs << endl;
	return 0;
}
