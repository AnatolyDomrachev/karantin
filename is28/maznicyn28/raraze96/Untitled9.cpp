#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

string funChanger(string a, int m, int n)
	{
	string bi = "";
	int c = 0;
	char b[a.size()];
	for (int i = 0; i < a.size(); i++)
		{
		
		if (i >= n - 1 && i < m + n - 1)
			{
			continue;
			}else
			{
			b[c] = a[i];
			c++;
			}
		}
	for (int i = 0; i < a.size() - m; i++)
		{
		bi += b[i];
		}
	return bi;
	}
int main()
	{
	string a, b;
	int m, n;
	ifstream file;
	file.open("txtin.txt");
	file >> a >> m >> n;
	b = funChanger(a, m, n);
	file.close();
	ofstream filec;
	filec.open("txtout.txt");
	filec << b.c_str() << '\n';
	filec.close();
	}