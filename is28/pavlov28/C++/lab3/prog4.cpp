#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	float x;
//Делится ли трёхзначное число на 4, если да то True, иначе False
	cout << "Число: ";
	cin >> x;
	x = fmod(x, 4);
	if (x == 0)
		cout << true << endl;
  	else 
		cout << false << endl;
	return 0;
}
