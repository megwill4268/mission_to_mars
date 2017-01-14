import sys
class Mission(object):
    def __init__(self):
        self.welcome = ("A tall long robot with a nametag reading 'Eugene' is smiling down at you.\n"
                        "'Welcome, congratulations on surviving hypersleep and arriving near mars.\n"
                        "We are ready to get into orbit around mars.'\n"
                        "You sit up and climb out of the hypersleep chamber. You walk over to the computer.\n")
        self.rock_gathering = ['ruby', 'crimson',  'scarlet']
        self.lichen_planting =  ['ruby', 'crimson',  'scarlet']
        self.main_goals = ['orbit Mars', 'land shuttle', self.rock_gathering , self.lichen_planting]
        self.astronaut = None
        self.mission_statement =  ("-----------------\n"
                                    "Mission to mars\n"
                                    "Objectives \n"

                                     "1. Successfully get into orbit around mars and release satelite\n"
                                     "2. Land shuttle with 80% structural integerety left and 60% fuel\n"
                                     "3. Pick up rock spemins from 3 locations and plant lychee\n"
                                     "-----------------\n\n")
        self.equipment = ("-----------------\n"
                          "Equipement\n"
                          "spacesuit (2)\n"
                          "robot (1)\n"
                          "rover (1)\n"
                          "lychee in  (4)\n"
                          "rock containers (4)\n"
                          "extra air packs (3 days)\n"
                          "food and water packs (2 days)\n"
                          "candy bars (2)\n"
                          "-----------------\n\n")


    def start(self):
        print(self.welcome)
        astronaut_name = raw_input("Please type your name to loginto computer and start orbit sequence.\n")
        astronaut = Astronaut(astronaut_name)
        print("welcome to main program %s, choose command from menu\n") % astronaut_name
        self.console_first_options()
        

    def console_first_options(self):
        choice = raw_input(("* mission objectives\n"
                            "* equipment\n"
                            "* start orbit sequence\n\n"))
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
        print("-----------------\n"
              "You have selected to start the orbit sequence.\n"
              "Thrusters moving, description. Spaceship in orbit.\n"
              "Satelite has been released into orbit.\n"
              "Please choose another command\n"
              "-----------------\n\n")
        self.main_goals.remove('orbit Mars')
        self.land_shuttle_choice()
        

    def land_shuttle_choice(self):
        choice = raw_input(("* mission objectives\n"
                            "* equipment\n"
                            "* land shuttle\n\n"))
        if "mission" in choice:
            print self.mission_statement
            self.land_shuttle_choice()
        elif "equipment" in choice:
            print self.equipment
            self.land_shuttle_choice()
        elif "land" in choice:
            shuttle = Shuttle()
            print("-----------------\n"
                  "You have selected to start automated land shuttle sequence. beginning release from main ship.\n"
                  "Shuttle detached, airlocks intact. Beginning descent.\n"
                  "Warning.\n"
                  "Danger.\n"
                  "Electromagnetic interference throwing off automated sequence.\n" 
                  "Aborting.\n"
                  "Pilot must take over manuel control. Adjust speed to land correctly\n."
                  "-----------------\n\n")
            self.land_shuttle(shuttle=shuttle)
        else:
            self.land_shuttle_choice()


    def land_shuttle(self, shuttle):
        while shuttle.distance != 0:
            msg = ("-----------------\n"
                   "Type thrusters to break with Retroburning.\n"
                   "Type fall to continue falling.\n"
                   "Shuttle {dist} from surface, speed {speed}, fuel {fuel}\n-----------------\n\n".format(dist=shuttle.distance, speed=shuttle.speed, fuel=shuttle.fuel))
            choice = raw_input(msg)
            if choice == "thrusters":
                shuttle.retroburn()
            elif choice == "fall":
                shuttle.fall()

        if shuttle.distance == 0:
            shuttle.cal_landing_damage()
            shuttle.cal_landing_success()
            print(shuttle.message)
            if shuttle.landed_successfully == False:
               sys.exit()
            else:
                self.main_goals.remove('land shuttle')
                print("-----------------\n"
                      "You pack up the rover with the help of the Eugene.\n"
                      "All supplies loaded you prepare to drive to your first site.\n"
                      "-----------------\n\n")
                self.site_choice()

    def site_choice(self):
        choice = raw_input("Choose:\n"
                        "* ruby valley\n"
                        "* crimson lake\n"
                        "* scarlet rock\n\n")    
        if "ruby" in choice:
            ruby = ruby_valley()
            self.site_missions(ruby)
        elif "crimson" in choice:
            crimson = crimson_lake()
            self.site_missions(crimson)
        elif "scarlet" in choice:
             scarlet = scarlet_rock()
             self.site_missions(scarlet)
        else:
             self.site_choice()

    def site_missions(self, loc):
        choices = 0
        while choices < 3:
            choice = raw_input(loc.options)
            if 'rock' in choice:
                choices += 1
                loc.gather_rocks()
                try:
                    self.rock_gathering.remove(loc.name)
                except Exception:
                    print ("already done\n")
            if 'plant' in choice:
                choices += 1
                choices += 1
                loc.plant_lichen()
                try:
                    self.lichen_planting.remove(loc.name)
                except Exception:
                    print ("already done\n")
            if 'explore' in choice:
                choices += 1
                loc.explore()
        if self.lichen_planting and self.rock_gathering:
            self.site_choice()
        else:
            self.main_goals.remove('rock gathering')
            self.main_goals.remove('lichen planting')
            print("That was hard work! All mission goals completed.\n")
            if loc.name != 'scarlet':
                print("That scarlet rock was nice, I should go take a break up there.\n")
                self.site_choice()
            else:
                print("I think I'll take a break here.\n")
                loc.take_break()



class Being(object):
   
   def __init__(self):
       self.name = None


class Human(Being):

   def __init__(self, name):
       self.name = name
       self.hungry = True
       self.sleepy = False
       super(Human, self).__init__()


class Astronaut(Human):
    def __init__(self, name):
        self.mission = Mission()
        self.name = name
        super(Astronaut, self).__init__(self.name)


class Alien(Being):
    def __init__(self, name):
        self.name = name
        super(Alien, self).__init__(self.name)


class Shuttle(object):
    def __init__(self):
        self.speed = 1000
        self.fuel = 100
        self.structural_integrity = 100
        self.speed_alteration = 200
        self.fuel_usuage = 10
        self.distance = 10000
        self.landed_successfully = False
        self.message = None

    def retroburn(self):
        "Not allowing negative speed, distance or fuel"
        if self.speed >= self.speed_alteration:
            self.speed -= self.speed_alteration
        else:
            self.speed = 0
        if self.fuel >= self.fuel_usuage:
            self.fuel -= self.fuel_usuage
        else:
            self.fuel = 0
        if self.distance >= 1000:
            self.distance -= 1000
        else:
            self.distance = 0

    def fall(self):
        if self.distance >= 2000:
            self.distance -= 2000
        else:
            self.distance = 0

    def cal_landing_damage(self):
        if self.speed != 0:
            self.structural_integrity -= (self.speed * 0.1)

    def cal_landing_success(self):
        if self.fuel < 60:
            self.landed_successfully = False
            self.message = ("You landed saftely but do not have enough fuel to make it back to the spaceship and return to Earth.\n"
                             "You plant the lychee and die watching strange stars dance.\n")
        elif self.structural_integrity <= 30:
            self.landed_successfully = False
            self.message = "You hit the surface too fast and explode in a blaze of glory.\n"
        elif (self.structural_integrity > 30) and (self.structural_integrity < 80):
            self.landed_successfully = False
            self.message = ("You hit the surface in a crumpled hull that no longer remotely resembles a shuttle.\n"
                             "You can no longer to make it back to the spaceship and return to earth.\n"
                             "You plant the lychee and die watching strange stars.\n")
        else:
            self.landed_successfully = True
            self.message = "Like a pro you gracefully swoop down onto the red marshain surface with a perfect landing.\n"


class Location(object):
    def __init__(self, name, msgs):
        self.name = name
        self.planting_completed = False
        self.rock_gathering = False
        self.msgs = {}
        self.options = ("* explore\n"
                        "* gather rocks\n"
                        "* plant lichen\n\n")

    def explore(self):
        print(self.msgs.get('explore'))

    def plant_lichen(self):
        print(self.msgs.get('plant'))
        self.planting_completed = True

    def gather_rocks(self):
        print(self.msgs.get('rock'))
        self.rock_gathering = True


class ruby_valley(Location):
    def __init__(self):
        self.msgs = { 'explore': ("walking through the valley the wind makes a lovely whistle,\n"
                      "you almost fancy you can hear a voice accomanying the wind in a high falceto.\n" 
                      "Finding nothing spectacular except the view you return to the rover.\n"), 
                      "plant": "you planted lychee, one small step towards an atmosphere\n",
                      "rock":"You gather serveral nice rock samples to be analyzed on earth\n"}
        self.name = 'ruby'
        super(ruby_valley, self).__init__(self.msgs, self.name)


class crimson_lake(Location):
    def __init__(self):
        self.msgs = { 'explore': ("you find a small footprint fossilized in the ground,\n" 
                       "it is a round paw with four round toe indentions, you carefully chizel out the\n"
                       "print fossil and place it in the spare rock container.\n"), 
                      "plant": "you planted lychee, one small step towards an atmosphere\n", 
                      "rock":"You gather serveral nice rock samples to be analyzed on earth\n"}
        self.name = 'crimson'
        super(crimson_valley, self).__init__(self.msgs, self.name)


class scarlet_rock(Location):
    def __init__(self):
        self.msgs = {'explore': ("The robot analyzes the area as you look down over the valley,\n"
                      "you notice to your right that some rocks are unusually square and organized,\n"
                      "hardly the work of erdoding due to wind or ancient streams.\n"), 
                      "plant": "you planted lychee, one small step towards an atmosphere\n", 
                      "rock": "You gather serveral nice rock samples to be analyzed on earth\n"}
        self.name = 'scarlet'
        super(scarlet_rock, self).__init__(self.msgs, self.name)

    def take_break(self):
        msg = ("You climb into the rover, seal in the pressure and take off your helmet.\n"
               "You eat a satisfying lunch and admire the view as you snack on a candy bar.\n"
               "You set it down to drink some water and it is not there when you look back,\n"
               "a little purple being is eating your candy bar!\n")
        print(msg)
        self.final_first_choice()

    def final_first_choice(self):
        choice = raw_input(("take back your candy bar\n"
                            "say hi\n"))
        if "candy" in choice:
            print (("The purple creature sadly hands you the candy bar and you eat the rest of it,\n"
                    "it's saliva poisons you and you die with the purple being looking very sad and worried.\n"))
            sys.exit()
        elif "hi" in choice:
            print("the purple being eats the rest of the candy bar and then points towards a big rock ahead.\n")
            self.final_second_choice()
        else:
            self.final_first_choice()

    def final_second_choice(self):
        choice = raw_input(("follow creature's point\n"
                         "have the robot eliminate the creature\n"))
        if "follow" in choice:
            print(("The rock disapears and you find you have driven into a street,\n"
                    "there is a whole city cloaked by a force field of sorts.\n"
                    "you put back on your helmet quickly as the purple creature tries to get out. \n"
                    "You follow it outside and are surrounded by purple beings.\n"))
            self.final_third_choice()
        elif "eliminate" in choice:
            print(("You return to earth with the alien body in the spare hibernation pod.\n"
                    "You are wildly popular but feel curious about that rock the rest of your life\n"))
        else:
            self.final_second_choice()

    def final_third_choice(self):
        choice = raw_input(("take your picture with aliens\n"
                         "try and capture an alien to take to earth\n"
                         "say hi\n"))
        if "hi" in choice:
            print(("they wave at you and the purple alien that was with you runs into a\n"
                    "building and comes back out with a suitcase and points to the rover.\n"
                    "You get into the rover and wave goodbye to the aliens.\n"
                    "You drive back to the shuttle and get into the hibernation pods.\n"
                    "You and the alien arrive heros to earth, splurp, the alien tours all the\n"
                    "great wonders of the world and then returns to mars on the next shuttle.\n"))
        if "picture" in choice:
             print( "you now have an awesome souvenier, way to go!\n")
        if "capture" in choice:
            print ("you fail and are imprisoned, forever :(\n")
            sys.exit()
        else:
            self.final_third_choice()