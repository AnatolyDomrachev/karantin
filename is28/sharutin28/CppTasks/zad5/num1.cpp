#include <iostream>
#include <vector>
#include <string>
#include <fstream>
//#include "stdafx.h"

using namespace std;

int main(int argc, char* argv[])
{
	int i;
	int j;
	ofstream fout("data.txt");
	int kot;
	for (i=0; i=3; i++)
	{
		for (j=0; j=3; j++)
		{
			
			fout << kot << " ";
	
		}	
	}
	fout.close();
	

	return 0;
}
