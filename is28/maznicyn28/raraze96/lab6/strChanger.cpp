#include <iostream>
#include <cmath>

using namespace std;

bool strChanger(string a,string b)
{
bool f = false;
int c = a.size() - b.size() + 1;
for (int i = 0; i <= c; i ++)
{
int g = 0;
if (a[i] == b[0]) { if (b.size() > 1){
	for (int j = i + 1; j < i + b.size(); j++) {
		if (a[j] == b[c+1]){
		c++;
		}else{
		c = 0;
		}
		
	}
	}
	if (c == b.size() - 1){
	f = true;
	}else{
	f = true;
	
}
}
}
return f;
}
int main(){
string a, b; 

cin >> a >> b;
bool c = strChanger(a, b);
cout << c << endl;
return 0;
}