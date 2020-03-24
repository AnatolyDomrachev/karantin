#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

static int a[4][4];
int masss(int& str, int& stl)
	{
	ifstream file;
	file.open("txtin1.txt");
	for (int i = 0; i < 4; i++)
		{
		for (int j = 0; j < 4; j++)
			{
			file >> a[i][j];
			}
		
		}
	file >> str >> stl;
	file.close();
	return 0;
	}

int 


int main()
	{
	int str, stl;
	masss(str, stl);
	for (int i = 0; i < 4; i++)
		{
		for (int j = 0; j < 4; j++)
			{
			cout << b[i][j] << " ";
			}
		cout << endl;
		}
	
	}