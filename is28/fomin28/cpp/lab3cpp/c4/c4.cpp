#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   
	int x,y;
	bool z;
	cout << "введите число ";
	cin >> x;
	y = fmod(x,4);
	z = y == 0;
	if (z==0) cout << "false" << endl;
	else cout << "true" << endl;
	
    return 0;
}
