def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b
	
def sub(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def mul(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b
	
def div(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b
	
print "Maths with just functions"

age = add(30,5)
height = sub(78,4)
weight = mul (90,2)
iq = div(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)

#for extra credit

print "Bonus round!"

what = add (age, sub (height, mul(weight,div(iq,2))))

print "That becomes:", what, "\n Can you do it by hand?"
