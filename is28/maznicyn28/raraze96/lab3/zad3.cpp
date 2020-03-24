#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
int x,sum = 0;
cin >> x;
for (int i = 0; i < 3; i++){
sum += x % 10;
x /= 10; 
}
cout << sum <<endl;
return 0;
}