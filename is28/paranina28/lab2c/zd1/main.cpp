#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{   float x1,y1,x2,y2,s;


    cout << "Введите х1 = ";
    cin >> x1;
    cout << "Введите y1 = ";
    cin >> y1;
    cout << "Введите х2 = ";
    cin >> x2;
    cout << "Введите y2 = ";
    cin >> y2;
    s = pow((x1-x2),2)+pow((y1-y2),2);
    s = sqrt(s);
    cout << fixed <<setprecision(3) <<"s = " <<s << endl;
    return 0;
}
