#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{   
	float l,cosinus,sinus;
	const double PI = 3.14149265;
	cout << "ввелите yгол (rad) ";
	cin >> l;
	cosinus = cos(l);
	sinus = sin(l);
	
    cout << "синyс yгла = "<< sinus << endl;
    cout << "косинyс yгла = "<< cosinus << endl;
    return 0;
}
