from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input ("> ")
	how_much = int(choice)
	if ValueError:
		dead("Man, learn to type a number.")
	elif how_much <50:
		print "Nice, you are not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard")


def bear_room():
	print "There is a bear here."
	print "The bear has a pot of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False 
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead ("The bear slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go now."
			bear_moved = True 
		elif choice == "taunt bear" and bear_moved:
			dead ("The bear is pissed and chews your legs off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I don't know what you are saying."
			
def cthulhu_room():
	print "Here you see the great Elder God Cthulhu."
	print "He, it, whatever, stares at you and you go insane"
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input ("> ")
	
	if "flee" in choice: 
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "there is a door to your right and to your left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()

