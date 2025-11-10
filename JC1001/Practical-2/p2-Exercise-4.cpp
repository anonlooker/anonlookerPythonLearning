/*4) Write a program that reverses the calculation performed in exercise 4.
That is, it should convert a temperature in degrees Celsius to degrees Fahrenheit.
Include in the output, the original value in Celsius that has been converted into
degrees Fahrenheit. (a simple way to perform this calculation is to multiply the
Celsius temperature by 9, divide by 5 and then add 32).*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    double celsiusTemp;
    // Ask for temperature in degrees Celsius
    cout<< "Enter temperature in degrees Celsius: ";
    cin>> celsiusTemp;
    // Convert Celsius to Fahrenheit
    double fahrenheitTemp = (celsiusTemp * 9 / 5) + 32;
    // Output the result
    cout<< celsiusTemp << " degrees Celsius is equal to " << fahrenheitTemp << " degrees Fahrenheit." << endl;

    return 0;
}
//p2-Exercise-4.cpp