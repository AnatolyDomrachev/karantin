#include <math.h>
#include <iostream>


#define PI 3.1415265
using namespace std;

int main()
{
	double R;
	cin >> R;
	
	cout << sin(R * PI/180) << endl;
	cout << cos(R * PI/180) << endl;

	return 0;
}
