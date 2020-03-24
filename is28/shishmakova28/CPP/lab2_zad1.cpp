/*vozrast = float(input("сколько вам лет? "))
print('Через 10 лет вам бóдет',vozrast+10)*/
#include  <iostream>
using namespace std;
int main()
{
int vozrast, voz10;
cout << "сколько вам лет?\n";
cin >> vozrast;
voz10 = vozrast+10;
cout << "Через 10 лет вам бóдет: " << voz10;
return 0;
}