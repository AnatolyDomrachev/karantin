#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	double x, i;
	x = modf(12.321, &i);
	
	printf("%f %f", i, x);
	
	return 0;

}


