/*print('Введите значение n')
N=int(input())
A=1
B=1
K=0

if N>=2:
	print(A)
	print(B)
if N==1:print(A)
if N<=0:print(0)

for i in range(0,N-2):
	C=A+B
	A=B
	B=C
	K=K+1
print(C)*/
#include  <iostream>

using namespace std;

int main()
{
	int A,B,C,K,chislo;
	cout << "Введите целое число \n ";
	cin >>chislo;
	schetchik=0;
	while (celchislo/2!=0)
	{
	schetchik=schetchik+1;
	celchislo=celchislo/2;
	}
	cout<<schetchik+1<<endl;
	return 0;
}
