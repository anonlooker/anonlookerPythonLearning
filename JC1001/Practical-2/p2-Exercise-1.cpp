/*1) Write a program which asks the user for their name and age and then calculates
the year of their birth and returns this information to the user.*/
#include <iostream>
#include <string>
#include <chrono>
using std::cin;
using std::cout;
using std::string;
using std::endl;

int main(void)
{
    string name;
    int age;
    // For the current year
    auto now = std::chrono::system_clock::now();
    std::time_t time_tNow_c = std::chrono::system_clock::to_time_t(now);
    int currentYear = 1900 + std::localtime(&time_tNow_c)->tm_year;
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