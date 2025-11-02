/*8)  Write a program that reverses the calculation performed in exercise 7, where the 
user enters a duration in seconds and the duration is returned to the user in days, 
hours, minutes, and seconds, with each unit of time printed on a separate line.*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    int totalSeconds;
    cout << "Enter duration in seconds: ";
    cin >> totalSeconds;

    int days = totalSeconds / 86400;
    totalSeconds %= 86400;
    int hours = totalSeconds / 3600;
    totalSeconds %= 3600;
    int minutes = totalSeconds / 60;
    int seconds = totalSeconds % 60;

    cout << "Duration:" << endl;
    cout << days << " days" << endl;
    cout << hours << " hours" << endl;
    cout << minutes << " minutes" << endl;
    cout << seconds << " seconds" << endl;

    return 0;
}
//p2-Exercise-8.cpp