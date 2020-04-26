#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

int** vvod(int M, int N)
{
	int** a = new int*[M];
	for(int i=0; i<M;i++)
		a[i] = new int[N];

	a[0][0] = 7;
	a[0][1] = 1;
	return a;
}

void vyvod(int** p, int M, int N)
{
	for(int i=0; i<M;i++)
		for(int j=0; j<N;j++)
			cout << p[i][j]<<"  ";
}

int main() 
{
	int M = 3;
	int N = 3;
	int** p = vvod(M,N);
	vyvod(p,M,N);

	for(int i=0; i<M;i++)
		delete(p[i]);
	delete(p);

	return 0;
}

