#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
//#include "stdafx.h"

using namespace std;

/* int main(int argc, char* argv[])
{

	ofstream fout("tomato.txt");
	fout << "1 4 5 6" << endl << "1 4 5 7" << endl << "1 4 5 6" << endl << "1 4 5 6" << endl;
	fout.close();
	
	return 0;
}  */

int main()
{
	
	int i;
	const int row = 4, column = 4;
	int array [row][column];
	string s;
	ifstream file("/home/is28/sharutin28/CppTasks/zad5/tomato.txt");
	//ofstream fout("cppstudio.txt", ios_base::in);
	while(getline(file, s))
	{
		for (int i = 0; i < row; i++)
		{
			
			int N[row];
			N >> array[i][i]
		
			
		}		
		cout << s << endl;
		//cout << v << endl;
		/*s += "+";
		cout << s << endl;*/
	
	}
	
	file.close();
	
	return 0;
}
