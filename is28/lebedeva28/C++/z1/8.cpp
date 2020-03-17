#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
//определить k-ю цифрy последовательности
	int k, x, i;
	x=0;
	i=1;
	cout << "k = " ;
	cin >> k;
	k--;
	while(x<=k)
{	
		if (k == x)
{
			cout << 1 << endl;
			return 0;
}
		x+=i;
		i++;
}
	cout << 0 << endl;
	return 0;
}
