#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	double S,A,B,C,Summa;

cout << "Введите трехзначное число: ";
cin >> S;

A=trunc(S/100);

B=trunc(S/10)-trunc(S/100)*10;

C=trunc(S)-trunc(S/10)*10;

Summa = A + B + C;

cout <<"Первая цифра: "<< A << " Вторая цифра: " << B << " Третья цифра: " << C << " Сyмма цифр:" << Summa << endl;

return 0;
}