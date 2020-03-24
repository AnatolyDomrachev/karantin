#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
int a[4][4];
int b, c;
for (int i = 0; i < 4; i++)
{
for (int j = 0; j < 4; j++)
{
cin >> a[i][j];
}
} 
cin >> b >> c;
for (int i = 0; i < 4; i++)
{
for (int j = 0; j < 4; j++)
{
if (i == b - 1){
int v = a[i][j];
a[i][j] = a[c - 1][j];
a[c - 1][j] = v;
}
}
} 
cout << a[0][0] << " " << a[0][1] << " " << a[0][2] << " " << a[0][3]<<endl;
cout << a[1][0] << " " << a[1][1] << " " << a[1][2] << " " << a[1][3]<<endl;
cout << a[2][0] << " " << a[2][1] << " " << a[2][2] << " " << a[2][3]<<endl;
cout << a[3][0] << " " << a[3][1] << " " << a[3][2] << " " << a[3][3]<<endl;
return 0;
}
