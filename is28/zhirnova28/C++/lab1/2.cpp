#include <string>
#include <iostream>

using namespace std;

struct age
{
	int age;
};
int main()
{
	struct age X[1];

	for(int i = 0; i< 1 ; i++)
	{
		cout << "Cколько вам лет? ";
		cin >> X[i].age;
	}

	for(int i = 0; i< 1 ; i++)
	{
		cout <<"Через 10 лет Вам бyдет: "<< X[i].age+10 << endl;
	}

	return 0;
}
