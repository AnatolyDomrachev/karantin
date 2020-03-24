#include <iostream>
#include <iomanip>
#include  <cmath>

using namespace std;

int main()
{
    int x1,x2,y1,y2;
    float ans;
    cin >> x1;
    cin >> y1;
    cin >> x2;
    cin >> y2;
    ans = sqrt(pow((x2-x1),2)+pow((y2-y1),2));
    cout << fixed << setprecision(3) << ans << endl;
    return 0;
}
