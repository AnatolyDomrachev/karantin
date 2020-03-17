#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
string s = "";
int k;
cin >> k;
for (int i = 0; i <= k; i++ )
{
s += to_string(i);
} 
cout << s[k - 1]<< endl;
return 0;
}