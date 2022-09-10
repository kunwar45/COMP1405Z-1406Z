colour = input("Enter the colour of the traffic light (red, green, yellow): ")

distance = float(input("What is the distance to the intersection (m): "))

speed = float(input("What is the speed of the car (m/s): "))

time = distance/speed

if colour == "green":
    print("Go")
elif colour == "red":
    if time <= 2:
        print("Go")
    else:
        print("Stop")
elif colour == "yellow":
    if time <= 5:
        print("Go")
    else:
        print("Stop")
else:
    print("Stop")

print(time)