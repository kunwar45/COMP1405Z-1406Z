'''
Pseudocode:

Take a string input from the user and store it in a variable (trafficLightColour)
Take a float input from the user and store it in a variable (metersToIntersection)
Take a float input from the user and store it in a variable (carMetersPerSecond)

Divide metersToIntersection by carMetersPerSecond and store it in timeToIntersection

If the light is "green" OR (the light is "yellow" AND timeToIntersection is less than or equal to 5)
OR (the light is "red" AND timeToIntersection is less than or equal to 2):
    Output "Go"
Else:
    Output "Stop"

'''
trafficLightColour = str(input("What is the colour of the traffic light at the intersection? "))
metersToIntersection = float(input("What is the distance to the intersection in meters? "))
carMetersPerSecond = float(input("What is the speed of the car in meters per second? "))

timeToIntersection = metersToIntersection/carMetersPerSecond

if trafficLightColour == "green" or (trafficLightColour == "yellow" and timeToIntersection<=5) or (trafficLightColour == "red" and timeToIntersection<=2):
    print("Go")
else:
    print("Stop")
