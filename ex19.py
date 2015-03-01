def cheese_and_crackers (cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man, you're ready for a party!"
	print "Get a blanket \n"
	
print "We can give numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can mix"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "And here I start experimenting."

cupboard_content = [[0,0,3,14],[1,0,0,20]]
fridge_content = [[4,2],[12,4],[15,24],[0,0]]
print "Which shelf of the cupboard are the crackers on?"
print 'top = 1, bottom = 2'
shelf_c = raw_input ('>')
shelf_c = int(shelf_c) - 1

print "This is the cracker content of each section of the cupboard"
print cupboard_content[shelf_c]
print "Which section (1-4)would you like to use?"
item_c = raw_input ('>')
item_c = int(item_c) - 1

print "Which shelf of the fridge do you look for cheese on?"
print """1 to 4 from top to bottom. 
\nKeep in mind there is no cheese on the bottom shelf"""
shelf_f = raw_input ('>')
shelf_f = int(shelf_f) - 1

if shelf_f <3:
	print "Which item would you like?"
	item_f = raw_input ("""L for left item or anything else for right
	\n >""")
	if item_f == 'L':
		item_f = 0
	else:
		item_f = 1
		
	print "Let's see what you have"
	cheese_and_crackers(
	fridge_content[shelf_f][item_f], cupboard_content[shelf_c][item_c])
	
	print "Your flatmate brought more cheese and crackers!"
	cheese_and_crackers(
	fridge_content[shelf_f][item_f] + 12, cupboard_content[shelf_c][item_c]+ 6)
else:
	print "I told you."
	print "Can't you do anything right?"
	print "Enjoy your cheeseless party"
	print "Dishonour on you."
	print "Dishonour on your cow!"
	
	
	
	
	
