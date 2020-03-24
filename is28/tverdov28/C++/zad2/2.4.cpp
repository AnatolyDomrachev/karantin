#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define SIZE 10

bool isAscendingSequence(vector<float>& v)
{
    for(int i=0; i<v.size()-1; i++)
        if(v[i] >= v[i+1])
            return false;
    return true;
}

int main()
{
    vector<float> v(SIZE);
    for(auto& e: v)
        cin >> e;

    cout << (isAscendingSequence(v) ? "Возрастающая последовательность" : "Невозрастающая последовательность") << endl;
    return 0;
}

