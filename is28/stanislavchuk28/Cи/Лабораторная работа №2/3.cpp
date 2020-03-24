#include <string>
#include <iostream>
#include <cmath>
#define PI 3.14159265

using namespace std;

double lenght( double R )
{
	return R=R*(PI/180);
}

int main()
{
	int R;
	cin >> R;
	double len = lenght(R);
	cout << len << endl;
	return 0;
}
