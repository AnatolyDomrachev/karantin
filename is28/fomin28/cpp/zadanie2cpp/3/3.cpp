#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   int a[10];
	int b,x;
	b = 0;
	
	for(int i=0; i < 10; i++)
	{
		cout << "ввелите число массива ";
	    cin >> a[i];
	}
	cout << "ввелите искомое число ";
	cin >> x;
	for(int i=0; i < 10; i++)
	{
		if(a[i]==x) {cout << "Число" << x << "есть в массиве"<< endl;b=1;}
		
	}
	if (b<1) cout << "такого числа нет в массиве"<< endl;
	return 0;
}
 
