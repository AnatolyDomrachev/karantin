#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int x;
	int a1; 
	int a2;
	int a3;
	
	cin >> x;
	
	a1 = x % 10;
	a2 = x / 10;
	a2 = a2 % 10;
	a3 = x / 100;
	
	cout << (a1 + a2 + a3) << endl;
	
	return 0;
	
}
