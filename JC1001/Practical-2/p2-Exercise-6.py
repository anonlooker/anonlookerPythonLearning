#6) The speed of light c is approximately 3 × 108meters per second. Write a
#program that asks the user to input a time in seconds and returns the distance
#that light travels in this time. Your program should output the distance in meters,
#kilometres, and miles.
timeSec = float(input("Enter time in seconds: "))
speedOfLight = 3e8  # speed of light in meters per second
distanceMeters = speedOfLight * timeSec
distanceKilometers = distanceMeters / 1000
distanceMiles = distanceMeters / 1609.34
print("Distance light travels in %f seconds:" % timeSec)
print("%f meters" % distanceMeters)
print("%f kilometers" % distanceKilometers)
print("%f miles" % distanceMiles)
#p2-Exercise-6.py