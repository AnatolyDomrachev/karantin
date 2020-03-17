#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int L;

cout << "Сколько Вам лет? ";
cin >> L;

if (L%10==1)
 {
 cout<<"Вам "<<L<<" "<<"Год"<<endl;
}

if (L%10==2 || L%10==3 || L%10==4)
{
 cout<<"Вам "<<L<<" "<<"Года"<<endl;
}

if (L%10==0 || L%10==5 || L%10==6 || L%10==7 || L%10==8 || L%10==9)
{
 cout<<"Вам "<<L<<" "<<"Лет"<<endl;
}

return 0;
}