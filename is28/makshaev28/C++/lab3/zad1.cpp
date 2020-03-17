#include <iostream>


using namespace std;

int main()
{
int c;
double x,y;

cout<< "Введите число"<< endl;
cin>>x;
c=int(x);
y=x-c;
cout<<"Целая часть="<<c<<"  Дробная часть="<<y<<"";
return 0;
}
