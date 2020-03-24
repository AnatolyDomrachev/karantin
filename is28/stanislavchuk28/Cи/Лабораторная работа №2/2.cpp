#include <string>
#include <iostream>
#include <cmath>

using namespace std;

double lenght( int x1, int y1, int x2, int y2 )
{
	return sqrt((double)(x2-x1)*(x2-x1) + (double)(y2-y1)*(y2-y1));
}

int main()
{
	int x1, y1, x2, y2;
	cin >> x1 >> y1 >> x2 >> y2;
	double len = lenght(x1, x2, y1, y2);
	cout << len << endl;
	return 0;
}
