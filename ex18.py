#like argv
def print_two(*args):
	arg1, arg2 = args 
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
#*args pointless, do this
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#just one argument
def print_one (arg1):
	print "arg1: %r" % arg1
	
#this one takes no arguments
def print_none ():
	print "I got nothin'."
x = [1,[2,3],4]	
print_two(x, "Shaw")
print_two_again ("Zed","Shaw")
print_one("First!")
print_none()