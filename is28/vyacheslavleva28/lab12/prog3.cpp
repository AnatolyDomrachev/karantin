#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int d;
	
	cin >> d;
	
	if ( d % 7 == 0 )  
	{ 
		cout << "пн" << endl;
	} else if ( d % 7 == 1 )
	{
		cout << "вт" << endl;
	} else if ( d % 7 == 2 )
	{
		cout << "ср" << endl;
	} else if ( d % 7 == 3 )
	{ 
		cout << "чт" << endl;
	} else if ( d % 7 == 4 )
	{
		cout << "пт" << endl;
	} else if ( d % 7 == 5 )
	{
		cout << "сб" << endl;
	} else 
	{
		cout << "вс" << endl;
	}
	
	return 0;
}
