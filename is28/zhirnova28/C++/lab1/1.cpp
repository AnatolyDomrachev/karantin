#include <string>
#include <iostream>

using namespace std;

struct kurs_age
{
	int age;
	int kurs;
};
int main()
{
	struct kurs_age X[1];

	for(int i = 0; i< 1 ; i++)
	{
		cout << "Cколько вам лет? ";
		cin >> X[i].age;

		cout << "На каком вы кyрсе? ";
		cin >> X[i].kurs;
	}

	for(int i = 0; i< 1 ; i++)
	{
		cout <<"Возраст когда вы закончите инститyт: "<< X[i].age+(5-X[i].kurs) << endl;
	}

	return 0;
}
