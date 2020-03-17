/*print('Введите число')
A=float(input())
B=A//1
C=A%1
print(B,' ',C)*/
#include  <iostream>
#include  <cmath>
using namespace std;
int main()
{
double chislo,celayachast,drobchast;
cout << "Введите дробное число\n";
cin >> chislo;
celayachast=trunc(chislo);
drobchast=chislo-celayachast;
cout<<"целая часть числа: "<<celayachast<<' '<<"дробная часть числа: "<<drobchast<<endl;
return 0;
}