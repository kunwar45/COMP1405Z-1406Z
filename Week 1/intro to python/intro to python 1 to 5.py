#1My Hello World program

from dis import dis
from turtle import distance


print('hello world')

#2 Basic input program
name = input("What is your name")
print("This is your name: " + name)

#3 Basic I/O calculation
name = input("Enter your name")
birth_year = int(input("What is your birth year"))
print("Hello " + name + ", you are " + str(2022 - (birth_year)) + " years old")

#4 Conversion Program, meters to kilometers
distance_in_meters = int(input("How many meters do you want to convert into kilometers? "))
distance_in_kilometers = distance_in_meters/1000
print(distance_in_meters, " meters converts to ", distance_in_kilometers, " in kilometers")

