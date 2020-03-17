/*vozrast = int(input('сколько вам лет? ')) 
kurs = int(input('На каком ты кóрсе?'))

print('Ваш возраст, когда вы закочите инститóт,',vozrast + (4-kurs))*/
#include  <iostream>
using namespace std;
int main()
{
int vozrast, kyrs, vupysk;
cout << "сколько вам лет?\n";
cin >> vozrast;
cout << "на каком ты кóрсе?\n";
cin >> kyrs;
vupysk = vozrast+4-kyrs;
cout << "Ваш возраст, когда вы закончите инститóт: " << vupysk;
return 0;
}
