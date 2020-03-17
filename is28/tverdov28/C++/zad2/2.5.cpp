#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define SIZE 10

bool findRepeat(vector<int>& v)
{
    for(int i=0; i<v.size()-1; i++)
        if(v[i] == v[i+1])
            return true;
    return false;
}

int main()
{
    vector<int> v(SIZE);
    for(auto& e: v)
        cin >> e;
    sort(v.begin(), v.end());
    cout << (findRepeat(v) ? "Есть повторения" : "Нет повторений") << endl;
    return 0;
}
