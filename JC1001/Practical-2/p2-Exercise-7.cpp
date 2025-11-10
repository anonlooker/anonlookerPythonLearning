/*7)  Write a program that first asks the user to enter a duration in days, hours, 
minutes, and seconds. Use a similar approach to exercise 6, where first the 
program will ask for the duration in days, followed by hours, minutes etc. Your 
program should then return the total number of seconds of the full duration 
entered.*/
#include <iostream>
#include <gmpxx.h>  //GNU Multiple Precision Arithmetic Library C++ wrapper
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    mpz_class days, hours, minutes, seconds;
    cout << "Enter duration in days: ";
    cin >> days;
    cout << "Enter duration in hours: ";
    cin >> hours;
    cout << "Enter duration in minutes: ";
    cin >> minutes;
    cout << "Enter duration in seconds: ";
    cin >> seconds;
    mpz_class totalSeconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds;
    cout << "Total duration in seconds: " << totalSeconds << endl;

    return 0;
}
//2-Exercise-7.cpp