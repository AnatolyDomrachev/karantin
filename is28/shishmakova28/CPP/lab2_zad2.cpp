/*import math
print('Введите координаты первой точки')
x1=int(input())
y1=int(input())
print('Введите координаты первой точки')
x2=int(input())
y2=int(input())
S=(y1-y2)**2+(x1-x2)**2
S=math.sqrt(S)
print('%.3f'%S)*/
#include  <iostream>
#include  <cmath>
using namespace std;
int main()
{
double x1,x2,y1,y2,rast;
cout << "Введите координаты первой точки\n";
cin >> x1 >> y1;
cout << "Введите координаты второй точки\n";
cin >> x2 >> y2;
rast=sqrt(pow((y1-y2),2)+pow((x1-x2),2));
rast=floor(rast*1000)/1000;
cout<<"резóльтат: "<<rast<<endl;
return 0;
}