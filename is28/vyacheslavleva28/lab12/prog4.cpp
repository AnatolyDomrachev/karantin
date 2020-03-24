#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int s;
	cin >> s;
	
	s = s % 4;
	
	switch (s)
	{
		case 0:
			cout << "True" << endl;
			break;
		default:
			cout << "False"	<< endl;
			break;
	}
	
	return 0;
}
