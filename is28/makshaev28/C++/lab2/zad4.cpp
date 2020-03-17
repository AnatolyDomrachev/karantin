#include <iostream>
#include <math.h>

using namespace std;

int main()
{
double x,si,co;
cout<< "Введите yгол"<< endl;
cin>>x;
x=x*3.14/180;
si=sin(x);
co=cos(x);
cout<<fixed;
cout.precision(1);
cout<<"sin="<<si<<"cos="<<co<<endl;
return 0;
}
