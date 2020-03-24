#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

int main()
{   int x[4],m[4],v[4];
	int a[4][4]={{1,2,3,4},{5,3,2,6},{4,3,5,2},{2,3,4,5}};
	cout <<"заполните таблицy"<<endl;
	cin >> a[0][0];
    cin >> a[0][1]; 
    cin >> a[0][2];
    cin >> a[0][3]; 
    cin >> a[1][0];
    cin >> a[1][1];
    cin >> a[1][2];
    cin >> a[1][3];
    cin >> a[2][0];
    cin >> a[2][1];
    cin >> a[2][2];
    cin >> a[2][3];
    cin >> a[3][0];
    cin >> a[3][1];
    cin >> a[3][2];
    cin >> a[3][3];
	cout <<"до:"<<endl;
	cout << a[0][0] << a[1][0] << a[2][0] << a[3][0] << endl;
	cout << a[0][1] << a[1][1] << a[2][1] << a[3][1] << endl;
	cout << a[0][2] << a[1][2] << a[2][2] << a[3][2] << endl;
	cout << a[0][3] << a[1][3] << a[2][3] << a[3][3] << endl;
	cout <<"какие столбцы поменять? " << endl; 
	cin >> m;
	cin >> v;
	cout << "После:" << endl;
	x=0;
	x=a[m-1];
	a[m-1]=a[v-1];
	a[v-1]=x;
	cout << a[0][0] << a[1][0] << a[2][0] << a[3][0] << endl;
	cout << a[0][1] << a[1][1] << a[2][1] << a[3][1] << endl;
	cout << a[0][2] << a[1][2] << a[2][2] << a[3][2] << endl;
	cout << a[0][3] << a[1][3] << a[2][3] << a[3][3] << endl;
	return 0;
}
