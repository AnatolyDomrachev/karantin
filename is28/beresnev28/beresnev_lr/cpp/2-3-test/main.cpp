#include <string>
#include <iostream>

using namespace std;


int main()
{
	int X[10];
    int  p = 0;
    int t = 0;
    int k = 0;

	for(int i = 0; i< 10 ; i++)
	{
		cout << "введите элемент массива ";
		cin >> X[i];
	}
    cout << "введите искомое число ";
    cin >> t;
	for(int f = 0; f< 10 ; f++)
	{
        k = X[f];
        if (t = k)
        {
            p=p+1;
        }

	}
	if (p = 0)
	{
	cout << "no" << endl;
	} else {
	cout << "yes" << endl;
	}

	return 0;
}
