#include <iostream>
#include <vector>

using namespace std;

#define SIZE 4

class Matrix
{
public:
    vector<vector<int>> matrix;
    Matrix(int n, int m)
    {
        for(int i=0;i<n;i++)
            matrix.push_back(vector<int>(m));
    }

    int max()
    {
        int max = matrix[0][0];
        for(auto& line: matrix)
            for(auto& c: line)
                if(c > max)
                    max = c;
        return max;
    }
    int min()
    {
        int min = matrix[0][0];
        for(auto& line: matrix)
            for(auto& c: line)
                if(c < min)
                    min = c;
        return min;
    }
};


int main()
{
    Matrix matrix(SIZE, SIZE);
    for(auto& line: matrix.matrix)
        for(auto& c: line)
            cin >> c;

    int maxValue = matrix.max(), minValue = matrix.min();
    cout << "max: " << maxValue
        << "\nmin: " << minValue
        <<"\nразность max и min: " << maxValue - minValue
        << endl;
    return 0;
}
