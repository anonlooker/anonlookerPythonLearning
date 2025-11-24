#include<iostream>
#include<string>
using std::cout; using std::endl; using std::cin;
using std::string;
class Book
{
    public:
        string isbn, name;
        int printIsbn()
        {
            cout<<"ISBN of "<< name <<" is "<<isbn;
            return 0;
        }
};

int main(void)
{
    Book whyNationsFails;
    whyNationsFails.isbn="1234567890";
    whyNationsFails.name="Why Nationals Fails";
    whyNationsFails.printIsbn();
}