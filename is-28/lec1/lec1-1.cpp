#include <iostream>

using namespace std;

struct pixel
{
    unsigned char b;
    unsigned char g;
    unsigned char r;
};

int main()
{
    struct pixel p_in;
    struct pixel *pp_in = &p_in;
    p_in.b = 5;
    cout << "Hello world!" << endl;
    return 0;
}