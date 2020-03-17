#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	int x1;
	int y1;
	int x2;
	int y2;
	
	cin >> x1;
	cin >> y1;
	cin >> x2;
	cin >> y2;
	
	double S = pow(x1-x2,2) + pow(y1-y2,2);
	
	cout << "S= " << S << endl;

	return 0;
}
