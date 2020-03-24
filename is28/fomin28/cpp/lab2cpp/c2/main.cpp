#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   float a,rad;
const double PI = 3.14149265;
    cout << "введите число градyсов ";
    cin >> a;
    rad = (a * PI)/180;
    cout << "В радианах  это = " << rad <<endl;
    return 0;
}

