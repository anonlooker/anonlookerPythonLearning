/*6) The speed of light c is approximately 3 × 10^8 meters per second. Write a
program that asks the user to input a time in seconds and returns the distance
that light travels in this time. Your program should output the distance in meters,
kilometres, and miles.*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    double timeSec;
    const double speedOfLight = 3e8; // speed of light in meters per second
    cout << "Enter time in seconds: ";
    cin >> timeSec;
    double distanceMeters = speedOfLight * timeSec;
    double distanceKilometers = distanceMeters / 1000;
    double distanceMiles = distanceMeters / 1609.34;
    cout << "Distance light travels in " << timeSec << " seconds:" << endl;
    cout << distanceMeters << " meters" << endl;
    cout << distanceKilometers << " kilometers" << endl;
    cout << distanceMiles << " miles" << endl;

    return 0;
}
//p2-Exercise-6.cpp