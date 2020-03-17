/*print('Введите целое число')
A=int(input())
K=0
while A//2!=0:
	K=K+1
	A=A//2
print(K+1)*/
#include  <iostream>

using namespace std;

int main()
{
	int celchislo,schetchik;
	cout << "Введите целое число \n ";
	cin >>celchislo;
	schetchik=0;
	while (celchislo/2!=0)
	{
	schetchik=schetchik+1;
	celchislo=celchislo/2;
	}
	cout<<schetchik+1<<endl;
	return 0;
}