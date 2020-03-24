#include <iostream>
#include <vector>
#include <string>


using namespace std;

int vvod(){
	int k;
	cin >> k;
	return k;
}

int raschet(int k){
	int x;
	
	vector<int> a;
	for (int i = 0; i < 90; i++){
		i = i+10;
		x = i/10;
		a.push_back(x);
		x = i%10;
		a.push_back(x);
		
	}
	int y;
		
	
	cout << a[k] << endl;
	return 0;

}

int main(){
	int pomidorka;
	pomidorka = vvod();
	raschet(pomidorka);
	return 0;
	
}
