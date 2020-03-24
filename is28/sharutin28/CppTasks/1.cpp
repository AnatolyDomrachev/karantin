#include <string>
#include <iostream>

using namespace std;

struct name_age
{
	int age;
	string name;
};

int main()
{
	struct name_age X[3];

	for(int i = 0; i< 3 ; i++)
	{
		cout << "как вас зовóт?";
		cin >> X[i].name;

		cout << "сколько вам лет?";
		cin >> X[i].age;
	}

	for(int i = 0; i< 3 ; i++)
	{
		cout <<"привет" << X[i].name << endl;
		cout <<"через 10 лет вам бóдет " << X[i].age+10 << endl;
	}

	return 0;
}
