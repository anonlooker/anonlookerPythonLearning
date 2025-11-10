/*2) Write a program which converts miles into kilometres. Your program should first
ask the user to enter a distance in miles to be converted and you should then
return the converted distance in kilometres. Include in the output, the original
value in miles that has been converted into kilometres. (1 kilometre is
approximately 0.6214 miles)*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    double miles;
    // Ask for distance in miles
    cout<< "Enter distance in miles: ";
    cin>> miles;
    // Convert miles to kilometres
    double kilometres = miles / 0.6214;
    // Output the result
    cout<< miles << " miles is equal to " << kilometres << " kilometres." << endl;

    return 0;
}
//p2-Exercise-2.cpp