#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
short nomer_dnya, den_nedeli;
cin >> nomer_dnya;
den_nedeli = fmod(nomer_dnya, 7);
if (den_nedeli == 0){cout << "Вс" << endl;}
else if (den_nedeli == 1){cout << "Пн" << endl;}
else if (den_nedeli == 2){cout << "Вт" << endl;}
else if (den_nedeli == 3){cout << "Ср" << endl;}
else if (den_nedeli == 4){cout << "Чт" << endl;}
else if (den_nedeli == 5){cout << "Пт" << endl;}
else if (den_nedeli == 6){cout << "Сб" << endl;}
return 0;
}