#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int s;
	cin >> s;
	
	s = s % 14;
	
	switch (s)
	{
		case 7:
			cout << "True" << endl;
			break;
		default:
			cout << "False"	<< endl;
			break;
	}
	
	return 0;
}
