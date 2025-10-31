/*7)  Write a program that first asks the user to enter a duration in days, hours, 
minutes, and seconds. Use a similar approach to exercise 6, where first the 
program will ask for the duration in days, followed by hours, minutes etc. Your 
program should then return the total number of seconds of the full duration 
entered.*/
//days = int(input("Enter duration in days: "))
//hours = int(input("Enter duration in hours: "))
//minutes = int(input("Enter duration in minutes: "))
//seconds = int(input("Enter duration in seconds: "))
//totalSeconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
//print("Total duration in seconds: %d" % totalSeconds)
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    int days, hours, minutes, seconds;
    cout << "Enter duration in days: ";
    cin >> days;
    cout << "Enter duration in hours: ";
    cin >> hours;
    cout << "Enter duration in minutes: ";
    cin >> minutes;
    cout << "Enter duration in seconds: ";
    cin >> seconds;

    int totalSeconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds;
    cout << "Total duration in seconds: " << totalSeconds << endl;

    return 0;
}
//2-Exercise-7.cpp