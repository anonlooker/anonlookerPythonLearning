/*3) Write a program which converts temperature in degrees Fahrenheit to degrees
#Celsius. Your program should include in the output, the original value in
#Fahrenheit that has been converted into degrees Celsius. (a simple way to
#perform this calculation is to deduct 32 from the Fahrenheit temperature, multiply
#by 5 and then divide by 9).*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    double fahrenheitTemp;
    // Ask for temperature in degrees Fahrenheit
    cout<< "Enter temperature in degrees Fahrenheit: ";
    cin>> fahrenheitTemp;
    // Convert Fahrenheit to Celsius
    double celsiusTemp = (fahrenheitTemp - 32) * 5 / 9;
    // Output the result
    cout<< fahrenheitTemp << " degrees Fahrenheit is equal to " << celsiusTemp << " degrees Celsius." << endl;

    return 0;
}
//p2-Exercise-3.py