/*5) Write a program that asks the user for the length of the side of a square and then
calculates the area and perimeter and returns these values to the user.*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    double sideLength;
    // Ask for the length of the side of the square
    cout<< "Enter the length of the side of the square: ";
    cin>> sideLength;
    // Calculate area and perimeter
    double area = sideLength * sideLength;
    double perimeter = 4 * sideLength;
    // Output the results
    cout<< "Area of the square: " << area << endl;
    cout<< "Perimeter of the square: " << perimeter << endl;

    return 0;
}
//p2-Exercise-5.cpp