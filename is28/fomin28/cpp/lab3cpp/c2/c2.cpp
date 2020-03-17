#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   int x,y,z,i,sum;
	
	cout << "введите трехзначное число ";
	cin >> x;
	i = fmod(x,10);
	y = fmod(x/10,10);
	z = fmod(x/100,10);
	sum = i+y+z;
	cout <<"сyмма чисел = " << sum << endl;
	
    return 0;
}
