the_count = [1,2,3,4,5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this for-loop goes through a list
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#we can to through mixed lists too
#but we use %r because we don't know the variable type

for i in change:
	print "I got %r" %i

#we can build lists

elements = []

for i in range (0,6):
	print "adding %d to the list" %i
	elements.append(i)

for i in elements: 
	print "element was: %d" %i
	
#reversed() is a thing.