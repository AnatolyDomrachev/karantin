#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   float x1,x2,y2,y1,dist,s;
    cout << "введите х1 ";
    cin >> x1;
    cout << "введите y1 ";
    cin >> y1;
    cout << "введите х2 ";
    cin >> x2;
    cout << "введите y2 ";
    cin >> y2;

    dist = pow((x2-x1),2) + pow((y2-y1),2);
    s = sqrt(dist);
    cout << fixed << setprecision(3) << "DISTANCE= " << s << endl;
    return 0;
}
