from sys import argv

script, filename = argv 
print filename

print "file %r is going to be erased." %filename
print "To cancel, hit CTRL-C (^C)."
print "To proceed, hit RETURN."

raw_input ("?")

print "Opening the file ..."
target = open(filename, 'w')

print "Truncating the file. Adios!"
target.truncate()

print "Input the lyrics of the hit retro single 'What is love' by Haddaway:"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = raw_input("line 4: ")

print "Writing input to file."

string = (line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 )
target.write (string)

target.close()

print "Here is what you wrote:"
print open(filename).read()

print "And finally, we close it."
target.close()