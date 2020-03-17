#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int x1;
	int x2;
	int y1;
	int y2;
	double S;
	
	cin >> x1;
	cin >> x2;
	cin >> y1;
	cin >> y2;
	
	S = pow(x1-x2,2)+pow(y1-y2,2);
	S = sqrt(S);
	cout << S << "\n";
	
	return 0;
}