#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//Определяет день недели по номерy дня в годy (1 - понедельник и тд.)
	cout << "Число: ";
	cin >> x;
	x = fmod(x, 7);
	if (x == 0)
		cout << 7 << endl;
  	else 
		cout << x << endl;
	return 0;
}



