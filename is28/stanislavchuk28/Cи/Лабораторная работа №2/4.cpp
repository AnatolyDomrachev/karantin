#include <string>
#include <iostream>
#include <cmath>
#define PI 3.14159265

using namespace std;

double lenght( double R, double a)
{
	return R=a*(PI/180);
}

int main()
{	int a, R, b;
	cin >> a;
	std::cout<<"Синyс yгла в градyсах:"<< sin(a) <<"    Синyс yгла в радианах:"<<sin(a*PI/180)<<std::endl;
	std::cout<<"Косинyс yгла в градyсах:"<< cos(a) <<"    Косинyc yгла в радианах:"<<cos(a*PI/180)<<std::endl;
	double len = lenght(R,a);
	cout << "В радианах:"<<len << endl;
	return 0;
}
