import sys
from classes import *



mission_statement= """Mission to mars

Objectives 

1. Successfully get into orbit around mars and release satelite
2. Land shuttle with 80% structural integerety left and 60% fuel
3. Pick up rock spemins from 3 locations and plant lychee
"""

equipment = """equipement
spacesuit (2)
robot (1)
rover (1)
lychee in  (4)
rock containers (4)
extra air packs (3 days)
food and water packs (2 days)
candy bars (2)
"""

print("A tall long robot with a nametag reading 'Eugene' is smiling down at you.")
print(" 'Welcome, congratulations on surviving hypersleep and arriving near mars.")
print(" We are ready to get into orbit around mars.")
print("You sit up and climb out of the hypersleep chamber. You walk over to the computer ")

astronaut_name = input("Please type your name to loginto computer and start orbit sequence.")

astronaut = Astronaut(astronaut_name)

print("welcome to main program %s, choose command from menu") % astronaut_name

def first_choice():
	choice = input("""mission objectives
	equiment
	start orbit sequence""")



first_choice()
if "mission" in choice:
	print mission_statement
	first_choice()
elif "equipment" in choice:
	print equipment
	first_choice()
elif "orbit" in choice:
	print("You have selected to start the orbit sequence. Thrusters moving, description. Spaceship in orbit. Satelite has been released into orbit. Please choose another command")
else:
	first_choice()

def second_choice():
	choice = input("""mission objectives
	equiment
	land shuttle""")





second_choice()
if "mission" in choice:
	print mission_statement
	second_choice()
elif "equipment" in choice:
	print equipment
	second_choice()
elif "land" in choice:
    print("""You have selected to start automated land shuttle sequence. Beging release from main ship.
     Shuttle detached, airlocks in tact. Beinging descent.
     Warning.
     Danger.
     Electro matic interference throwing off automated sequence. 
     Aborting.
     Pilot must take over manuel control. Adjust speed to land correctly.""")
    shuttle = Shuttle()
else:
	second_choice()

def third_choice():
    choice = input("""Type thrusters to break with Retroburning. Type fall to continue falling.
    	               Shuttle %s from surface, speed %s, fuel %s""") % (shuttle.distance, shuttle.speed, shuttle.fuel)

while shuttle.distance != 0:
    third_choice()
	if choice == "thrusters":
		shuttle.retroburn()
	elif choice == "fall":
		shuttle.fall()

if shuttle.distance == 0:
	shuttle.cal_landing_damage()
	print shuttle.message
	if shuttle.landed_successfully == False:
		sys.exit()

choice = input(""""You pack up the rover with the help of Enrique the robot. 
All supplies loaded you prepare to drive to your first site.
Choose:
ruby valley
crimson lake
scarlet rock""")




