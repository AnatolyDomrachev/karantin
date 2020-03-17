/*print('Введите трехзначное число')
A=int(input())
B=A%10
C=A//100
D=(A//10)%10
print(B+C+D)*/
#include  <iostream>
#include  <cmath>

using namespace std;

int main()
{
	double cifra1,cifra2,cifra3,chislo,sum;
	cout << "Введите трехзначное число\n";
	cin >> chislo;
	cifra1=trunc(chislo/100);
	cifra2=trunc(chislo/10)-trunc(chislo/100)*10;
	cifra3=chislo-trunc(chislo/10)*10;
	sum=cifra1+cifra2+cifra3;
	cout<<"сóмма цифр = "<<sum<<endl;
	return 0;
}