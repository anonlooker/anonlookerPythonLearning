#include<iostream>
#include<string>
using std::cout; using std::endl; using std::cin;
using std::string;
class object
{
    public:
        string name;
        int printName()
        {
            cout << "Name is " << name << endl ;
            return 0;
        }
};
class Book: public object
{
    public:
        string isbn;
        int printIsbn()
        {
            cout << "ISBN of \"" << name << "\" is " << isbn << endl ;
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