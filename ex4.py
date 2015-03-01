# number of cars
cars = 100
#numbers of spaces per car 
spaces_in_a_car = 4
# number of drivers 
drivers = 30
#number of passengers
passengers = 90
cars_not_driven = cars - drivers
#every driver drives a car
cars_driven = drivers
#calculated in people
carpool_capacity = cars_driven * spaces_in_a_car
average_passengers_per_car = passengers / cars_driven 

print "There are", cars, "cars available."

print "there are only", drivers, "drivers available."

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "people in each car"


