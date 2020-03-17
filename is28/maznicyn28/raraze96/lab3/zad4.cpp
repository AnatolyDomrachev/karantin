#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
int s, k, summ;
cout << "ведите трёхзнчное число" << endl;
cin >> s;
k = s % 10;
s = s / 10;
summ = k;
k = s % 10;
s = s / 10;
summ += k + s;
cout << summ << endl;

return 0;
}
