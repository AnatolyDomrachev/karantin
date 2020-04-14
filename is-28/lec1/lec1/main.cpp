#include <iostream>

using namespace std;

struct book
{
    char author[50];
    int year;
    int pages;
};

int main()
{
    struct book Books[5];
    for(int i=0; i<5; i++)
    {
        cout << "Введите автора";
        cin >> Books[i].author;
    }
    cout << "Hello world!" << endl;
    return 0;
}
