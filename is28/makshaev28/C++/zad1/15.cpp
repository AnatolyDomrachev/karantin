#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{ 
int c=1;
int p=0;
int s=0;
int t=0;
while( c<=1000)
{
  s=s+c;
  t=c;
  c=c+p;
  p=t;}

cout<<"Сyмма чисел Фибоначи не превышающих 1000="<<s<<endl;
return 0;	
}
