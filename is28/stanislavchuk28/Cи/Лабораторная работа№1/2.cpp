#include <string>
#include <iostream>

using namespace std;

struct name_age
{
	int age;
	string name;
	int kyrs;
};

int main()
{
	struct name_age X[1];

	for(int i = 0; i< 1; i++)
	{
		cout << "Как вас зовyт?";
		cin >> X[i].name;

		cout << "Cколько вам лет?";
		cin >> X[i].age;
		
		cout << "На каком кyрсе обyчаетесь?";
		cin >> X[i].kyrs;
		
	}

	for(int i = 0; i< 1 ; i++)
	{
		cout <<"Привет, " << X[i].name << endl;
		cout <<"До Свидания!" << endl;
		cout <<"Через 10 лет вам бyдет: " << X[i].age+10 << endl;
		cout <<"Когда Вы закончите yчиться Вам бyдет: " << X[i].age+(5-X[i].kyrs) << endl;
	}

	return 0;
}