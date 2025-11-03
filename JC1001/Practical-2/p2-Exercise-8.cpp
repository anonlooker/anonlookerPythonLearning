/*8)  Write a program that reverses the calculation performed in exercise 7, where the 
user enters a duration in seconds and the duration is returned to the user in days, 
hours, minutes, and seconds, with each unit of time printed on a separate line.*/
#include <iostream>
#include <gmpxx.h>  //GNU Multiple Precision Arithmetic Library C++ wrapper
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    mpz_class totalSeconds;
    cout << "Enter duration in seconds: ";
    cin >> totalSeconds;
    mpz_class days = totalSeconds / 86400;
    totalSeconds %= 86400;
    unsigned hours = totalSeconds.get_ui() / 3600;
    totalSeconds %= 3600;
    unsigned minutes = totalSeconds.get_ui() / 60;
    unsigned seconds = totalSeconds.get_ui() % 60;

    cout << "Duration:" << endl;
    cout << days << " days" << endl;
    cout << hours << " hours" << endl;
    cout << minutes << " minutes" << endl;
    cout << seconds << " seconds" << endl;

    return 0;
}
//p2-Exercise-8.cpp