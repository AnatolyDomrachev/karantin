#include <string>
#include <iostream>

using namespace std;

int main()
{
	string name;
	int vozrast;
	
	
	cout << "как вас зовóт?";
	cout << "сколько вам лет?";

	cin >> name;
	cin >> vozrast;
	
	cout << "привет, " << name << endl;
	cout << "вам, " << vozrast << endl;

	return 0;
}
