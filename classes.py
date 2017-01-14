class Mission(object):
	def __init__(self):
        self.welcome = ("""A tall long robot with a nametag reading 'Eugene' is smiling down at you.
'Welcome, congratulations on surviving hypersleep and arriving near mars.
We are ready to get into orbit around mars.'
You sit up and climb out of the hypersleep chamber. You walk over to the computer.""")
		self.rock_gathering = ['ruby', 'crimson',  'scarlet']
		self.lichen_planting =  ['ruby', 'crimson',  'scarlet']
		self.main_goals = ['orbit Mars', 'land shuttle', rock_gathering , lichen_planting]	]
		self.astronaut = None
	    self.mission_statement =  """Mission to mars
Objectives 

1. Successfully get into orbit around mars and release satelite
2. Land shuttle with 80% structural integerety left and 60% fuel
3. Pick up rock spemins from 3 locations and plant lychee
"""
        self.equipment = """equipement
spacesuit (2)
robot (1)
rover (1)
lychee in  (4)
rock containers (4)
extra air packs (3 days)
food and water packs (2 days)
candy bars (2)
"""



    def start(self):
    	print(self.welcome)
    	astronaut_name = input("Please type your name to loginto computer and start orbit sequence.")
    	astronaut = Astronaut(astronaut_name)
    	print("welcome to main program %s, choose command from menu") % astronaut_name
        self.console_first_options()
		

	def console_first_options(self):
		choice = input("""mission objectives
		equiment
		start orbit sequence""")
		if "mission" in choice:
			print self.mission_statement
			self.console_first_options()
		elif "equipment" in choice:
			print self.equipment
			self.console_first_options()
		elif "orbit" in choice:
			 self.orbit()
		else:
			self.console_first_options()

	def orbit(self):
        print("""You have selected to start the orbit sequence. 
        	Thrusters moving, description. Spaceship in orbit. 
        	Satelite has been released into orbit.
        	Please choose another command""")
        self.main_goals.remove('orbit Mars')
        self.land_schuttle_choice()
		

	def land_schuttle_choice(self):
		choice = input("""mission objectives
		equiment
		land shuttle""")
		console_second_options()
		if "mission" in choice:
			print self.mission_statement
			self.land_schuttle_choice()
		elif "equipment" in choice:
			print self.equipment
			self.land_schuttle_choice()
		elif "land" in choice:
		    shuttle = Shuttle()
		    print("""You have selected to start automated land shuttle sequence. Beging release from main ship.
     Shuttle detached, airlocks in tact. Beinging descent.
     Warning.
     Danger.
     Electromagnetic interference throwing off automated sequence. 
     Aborting.
     Pilot must take over manuel control. Adjust speed to land correctly.""")
		    land_schuttle()
		else:
			self.land_schuttle_choice()


	def land_schuttle(self):
		while shuttle.distance != 0:
	        choice = input("""Type thrusters to break with Retroburning. Type fall to continue falling.
    	               Shuttle %s from surface, speed %s, fuel %s""") % (shuttle.distance, shuttle.speed, shuttle.fuel)
		if choice == "thrusters":
			shuttle.retroburn()
		elif choice == "fall":
			shuttle.fall()

		if shuttle.distance == 0:
			shuttle.cal_landing_damage()
			print shuttle.message
			if shuttle.landed_successfully == False:
				sys.exit()
		    else:
		    	self.main_goals.remove('land shuttle')
		    	print("""You pack up the rover with the help of the robot. 
                     All supplies loaded you prepare to drive to your first site.""")
		    	site_choice()

    def site_choice(self);
    	choice = input(""""Choose:
                           ruby valley
                           crimson lake
                           scarlet rock""")    
    	if "ruby" in choice:
    		ruby = ruby_valley()
    	elif "crimson" in choice:
    		crimson = crimson_lake()
    	elif "scarlet" in choice:
    		scarlet = scarlet_rock()
    	else:
    		site_choice()

    def site_missions(self, loc, name):
        choices = 0
        while choices < 3:
	        choice = input(loc.options)
	        if 'rock' in choice:
	        	choices += 1
	        	loc.gather_rocks()
	        	try:
	        		self.rock_gathering.remove(loc.name)
	        	except Exception:
	        		print ("already done")
	        if 'plant' in choice:
	        	choices += 1
	        	choices += 1
	        	loc.plant_lichen()
	        	try:
	        		self.lichen_planting.remove(loc.name)
	        	except Exception:
	        		print ("already done")
	        if 'explore' in choice:
	        	choices += 1
	        	loc.explore()
        if self.lichen_planting and self.rock_gathering:
	        site_choice()
	    else:
	    	self.main_goals.remove('rock gathering')
	    	self.main_goals.remove('lichen planting')
	    	print("That was hard work! All mission goals completed.")
	    	if loc.name != 'scarlet':
	    		print("That scarlet rock was nice, I should go take a break up there.")
	    		site_choice()
	    	else:
	    		print("I think I'll take a break here.")
	    		loc.take_break()


	def goals_completed(self):
		if goals_completed < total_goals:
			return False
		elif goals_completed == total_goals:
			return True





class Being(object):
   
   def __init__(self):
       self.name = None


class Human(Being);

   def __init__(self, name):
       self.name = name
       self.hungry = True
       self.sleepy = False
       super(Human, self).__init__()


class Astronaut(Human):
	def __init__(self):
		self.mission = Mission()


class Alien(Being):
	def __init__(self, name):
		self.name = name


class Shuttle(object):
	def __init__(self):
		self.speed = 1000
		self.fuel = 100
		self.structural_integrity = 100
		self.speed_alteration = 200
		self.fuel_usuage = 10
		self.distance = 10000
		self.landed_successfully = False
		self.message = ""

	def retroburn(self):
		self.speed -= speed_alteration
		self.fuel -= self.fuel_usuage
		self.distance -= 1000

	def fall(self):
		self.distance -= 2000

	def cal_landing_damage(self):
		if speed != 0:
			self.structural_integrity -= (speed * 0.1)

	def cal_landing_success(self):
		if self.fuel < 60:
            self.landed_successfully = False
            self.message = """You landed saftely but do not have enough fuel to make it back to the spaceship and return to Earth. 
                              You plant the lychee and die watching strange stars."""
		elif self.structural_integrity <= 30:
			self.landed_successfully = False
			self.message = "You hit the surface too fast and explode in a blaze of glory."
		elif (self.structural_integrity > 30) and (self.structural_integrity < 80):
			self.landed_successfully = False
			self.message = """You hit the surface in a crumpled hull that no longer remotely resembles a shuttle.
			 You can no longer to make it back to the spaceship and return to earth. 
			 You plant the lychee and die watching strange stars."""
		else:
			self.landed_successfully = True
			self.message = "Like a pro you gracefully swoop down onto the red marshain surface with a perfect landing."


class Location(object):
	def __init__(self):
		self.name = name
		self.planting_completed = False
		self.rock_gathering = False
		self.msgs = {}
		self.options = """explore
		                  gather rocks
		                  plant lichen"""

    def explore(self):
    	msg= None
        print(msg.get('explore'))

    def plant_lichen(self):
    	msg= None
        print(msg.get('plant'))
        self.planting_completed = True

    def gather_rocks(self):
    	msg= None
        print(msg.get('rock'))
        self.rock_gathering = True


class ruby_valley(Location):
    def __init__(self):
    	self.msgs = { 'explore': """walking through the valley the wind makes a lovely whistle,
    	 you almost fancy you can hear a voice accomanying the wind in a high falceto. 
    	 Finding nothing spectacular except the view you return to the rover.""", "plant": "you planted lychee, one small step towards an atmosphere",
    	 "rock":"You gather serveral nice rock samples to be analyzed on earth"}
    	 self.name = 'ruby'
    	super(ruby_valley, self).__init__(self.msgs, self.name)


class crimson_lake(Location):
	def __init__(self):
    	self.msgs = { 'explore': """you find a small footprint fossilized in the ground, 
    	it is a round paw with four round toe indentions, you carefully chizel out the
    	 print fossil and place it in the spare rock container.""", 
    	 "plant": "you planted lychee, one small step towards an atmosphere", 
    	"rock":"You gather serveral nice rock samples to be analyzed on earth"}
    	self.name = 'crimson'
    	super(crimson_valley, self).__init__(self.msgs, self.name)


class scarlet_rock(Location):
	def __init__(self):
		self.msgs = {'explore': """The robot analyzes the area as you look down over the valley,
		 you notice to your right that some rocks are unusually square and organized, 
		 hardly the work of erdoding due to wind or ancient streams.""", 
		 "plant": "you planted lychee, one small step towards an atmosphere", 
		"rock": "You gather serveral nice rock samples to be analyzed on earth"}
		self.name = 'scarlet'
		super(scarlet_rock, self).__init__(self.msgs, self.name)

	def take_break(self):
		msg = """You climb into the rover, seal in the pressure and take off your helmet.
		 You eat a satisfying lunch and admire the view as you snack on a candy bar.
		  You set it down to drink some water and it is not there when you look back,
		  a little purple being is eating your candy bar!"""
		print msg
		self.final_first_choice()

	def final_first_choice(self):
		choice = input("""take back your candy bar
			say hi""")
		if "candy" in choice:
			print """The purple creature sadly hands you the candy bar and you eat the rest of it, 
			it's saliva poisons you and you die with the purple being looking very sad and worried."""
			sys.exit()
		elif "hi" in choice:
	        print("""the purple being eats the rest of the candy bar and then points towards a big rock ahead.""")
			self.final_second_choice()
		else:
			self.final_first_choice()

	def final_second_choice(self):
		choice = input("""follow creature's point
		 have the robot eliminate the creature""")
		if "follow" in choice:
			print("""The rock disapears and you find you have driven into a street, 
			there is a whole city cloaked by a force field of sorts. 
			you put back on your helmet quickly as the purple creature tries to get out. 
			You follow it outside and are surrounded by purple beings.""")
			self.final_third_choice()
		elif "eliminate" in choice:
			print("""You return to earth with the alien body in the spare hibernation pod. 
				You are wildly popular but feel curious about that rock the rest of your life""")
		else:
			self.final_second_choice()

	def final_third_choice(self):
		choice = input("""take your picture with aliens
			try and capture an alien to take to earth
			say hi""")
		if "hi" in choice:
			print("""they wave at you and the purple alien that was with you runs into a
			 building and comes back out with a suitcase and points to the rover. 
			 You get into the rover and wave goodbye to the aliens.
			  You drive back to the shuttle and get into the hibernation pods. 
			  You and the alien arrive heros to earth, splurp, the alien tours all the
			   great wonders of the world and then returns to mars on the next shuttle.""")
		if "picture" in choice:
			 print( "you now have an awesome souvenier, way to go!")
		if "capture" in choice:
			print ("you fail and are imprisoned, forever :(")
			sys.exit()
		else:
			self.final_third_choice()