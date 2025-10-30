/*1) Write a program which asks the user for their name and age and then calculates
the year of their birth and returns this information to the user.*/
#include <iostream>
#include <string>
#include <ctime>
using std::cin;
using std::cout;
using std::string;
using std::endl;

int main(void)
{
    string name;
    int age;
    // For the current year
    time_t t = time(0);
    tm* now = localtime(&t);
    int currentYear = now->tm_year + 1900;
    // Ask for name
    cout<< "What is your name? ";
    getline(cin, name);
    // Ask for age
    cout<< "How old are you? ";
    cin>> age;
    // Calculate year of birth
    int birthYear = currentYear - age;
    // Output birthYear
    cout<< "Hello " << name << ". Your birth year is " << birthYear << "." << endl;

    return 0;
}
//p2-Exercise-1.cpp