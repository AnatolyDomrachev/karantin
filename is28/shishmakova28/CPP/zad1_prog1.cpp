/*print('Введите три числа')
A=float(input())
B=float(input())
C=float(input())
if A>B and A>C : print(A)
elif B>A and B>C: print(B)
else:print(C)*/
#include  <iostream>

using namespace std;

int main()
{
	int A,B,C;
	cout << "Введите три числа \n ";
	cin >>A>>B>>C;
	if (A>B and A>C){cout<<A<<endl;}
	if (B>A and B>C){cout<<B<<endl;}
	else {cout<<B<<endl;}
	return 0;
}