comparison_value = 12
increment_value = 3

def iterated_appending_while(comparison_value, increment_value):
	i = 0
	numbers = []
	while i <comparison_value:
		print "At the top i is %d" % i 
		numbers.append(i)
		i = i+increment_value 
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
	
	print "The numbers: "
	for num in numbers: 
		print num
		
iterated_appending_while (comparison_value, increment_value)

def iterated_appending_for (comparison_value, increment_value):
	i = 0
	numbers = []
	for i in range(comparison_value):
		print "At the top i is %d" % i 
		numbers.append(i)
		i = i+increment_value 
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
		
	print "The numbers: "
	for num in numbers: 
		print num
		
iterated_appending_for (comparison_value, increment_value)