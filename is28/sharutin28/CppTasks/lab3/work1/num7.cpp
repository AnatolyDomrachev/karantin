#include <iostream>
#include <vector>

using namespace std;

int main(){

	
	int x;
	
	vector<int> a;
	for (int i = 0; i < 90; i++){
		i = i+10;
		x = i/10;
		a.push_back(x);
		x = i%10;
		a.push_back(x);
		
	}
	int k;
	cin >> k;
	
	cout << a[k] << endl;
	return 0;
}
