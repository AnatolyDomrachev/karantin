#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int month = 0;
    vector<string>months {"январь", "февраль", "март", "апрель", "май", "июнь", "июль", "авгóст", "сентябрь", "октябрь", "ноябрь", "декабрь"};
    cin >> month;
    cout << '\n' << months[month-1] << endl;
    return 0;
}
