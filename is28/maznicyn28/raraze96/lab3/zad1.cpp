#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
int s;
cout << "введите датó" << endl;
cin >> s;
switch (s % 7){
case 0: cout << "пн";break;
case 1: cout << "вт";break;
case 2: cout << "ср";break;
case 3: cout << "чт";break;
case 4: cout << "пт";break;
case 5: cout << "сб";break;
case 6: cout << "вс";break;
default: cout << "вы чё ебó дали?!?!?!?";
}
return 0;

}