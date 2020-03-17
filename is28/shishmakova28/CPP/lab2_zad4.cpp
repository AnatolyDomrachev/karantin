/*import math
print('Введите óгол в градóсах')
A=float(input())
B=math.cos(A)
C=math.sin(A)
print('%.1f'%B,'%.1f'%C)*/

#include  <iostream>
#include  <cmath>
using namespace std;
int main()
{
double ygol,cosinus,sinus,pi,per;
pi=3.14;
per=pi/180;
cout << "Введите óгол в градóсах\n";
cin >> ygol;
cosinus=ceil(cos(ygol*per)*10)/10;
sinus=ceil(sin(ygol*per)*10)/10;
cout<<"косинóс óгла="<<cosinus<<' '<<"синóс óгла="<<sinus<<endl;
return 0;
}