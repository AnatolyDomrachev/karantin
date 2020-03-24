#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	double x1,x2,y1,y2,S;

cout << "Введите первyю координатy х: ";
cin >> x1;

cout << "Введите первyю координатy y: ";
cin >> y1;
		
cout << "Введите вторyю координатy х: ";
cin >> x2;

cout << "Введите вторyю координатy y: ";
cin >> y2;
		
S=sqrt(pow((x2-x1),2)+pow((y2-y1),2));


cout <<"Расстояние равно: "<< S << endl;

return 0;
}