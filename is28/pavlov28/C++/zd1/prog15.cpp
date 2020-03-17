#include <string>
#include <iostream>

using namespace std;

int main()
{
	int S, b, c, b1;
//Вычислить S – сумму всех чисел Фибоначчи, которые не превосходят 1000.
	b = c = 1;
	S = 1;
	while (c <= 1000) 
		{
		S = S + c;
		b1 = b;
		b = c;
		c = b1 + c;
		}
	cout << "Сyмма всех чисел Фибоначчи, которые не превосходят 1000 равна " << S << endl; 	
	return 0;
}

