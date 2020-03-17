/*import math
print('Введите число')
B=float(input())
B=math.radians(B)
print('%e'%B)*/

#include  <iostream>
using namespace std;
int main()
{
double chislo,P,vyvod;
P=3.14;
cout << "óгол в градóсах: ";
cin >> chislo;
vyvod=chislo*P/180;
cout << "óгол в радианах: "<<vyvod<<endl;
return 0;
}
