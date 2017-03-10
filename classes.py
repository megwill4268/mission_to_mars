import sys


class Mission(object):
    def __init__(self):
        self.welcome = ("A tall long robot with a name-tag reading 'Eugene' is smiling down at you.\n"
                        "'Welcome, congratulations on surviving hyper-sleep and arriving near mars.\n"
                        "We are ready to get into orbit around mars.'\n"
                        "You sit up and climb out of the hypersleep chamber. You walk over to the computer.\n")
        self.astronaut = None
        self.mission_statement = ("-----------------\n"
                                  "Mission to mars\n"
                                  "Objectives \n"
                                  "1. Successfully get into orbit around mars and release satellite\n"
                                  "2. Land shuttle with 80% structural integrity left and 60% fuel\n"
                                  "3. Pick up rock specimens and plant lichen\n"
                                  "-----------------\n\n")
        self.equipment = ("-----------------\n"
                          "Equipment\n"
                          "spacesuit (2)\n"
                          "robot (1)\n"
                          "rover (1)\n"
                          "lichen planting kits (4)\n"
                          "rock containers (4)\n"
                          "extra air packs (3 days)\n"
                          "food and water packs (2 days)\n"
                          "candy bars (2)\n"
                          "satellite (1)\n"
                          "-----------------\n\n")

    def start(self):
        print(self.welcome)
        astronaut_name = raw_input(("-----------------\n"
                                    "Please type your name to log into the main computer and start orbit sequence.\n"
                                    "-----------------\n\n"))
        astronaut = Astronaut(astronaut_name)
        print(("-----------------\n"
               "welcome to main program %s, choose command from menu\n-----------------\n\n")) % astronaut.name
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
              "Automated sequence enabled, moving into Maritain orbit.\nCorrecting\nSpaceship in orbit.\n"
              "Releasing satellite\n"
              "Satellite has been released into orbit.\n"
              "Please choose another command\n"
              "-----------------\n\n")
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
                  "You have selected to start automated shuttle landing sequence.\nInitiating release from main ship.\n"
                  "Shuttle detached, airlocks intact.\nBeginning descent.\n"
                  "Warning.\n"
                  "Danger.\n"
                  "Electromagnetic interference throwing off automated sequence.\n"
                  "Aborting.\n"
                  "Pilot must take over manual control. Adjust speed to land correctly.\n")
            self.land_shuttle(shuttle=shuttle)
        else:
            self.land_shuttle_choice()

    def land_shuttle(self, shuttle):
        while shuttle.distance != 0:
            msg = ("Type 'break' to break with Retroburning.\n"
                   "Type 'fall' to continue falling.\n"
                   "Shuttle distance from surface: {dist}, speed {speed}, fuel {fuel}%\n-----------------\n\n".format(
                    dist=shuttle.distance, speed=shuttle.speed, fuel=shuttle.fuel))
            choice = raw_input(msg)
            if choice == "break":
                shuttle.retroburn()
            elif choice == "fall":
                shuttle.fall()

        if shuttle.distance == 0:
            shuttle.cal_landing_damage()
            shuttle.cal_landing_success()
            print(shuttle.message)
            if not shuttle.landed_successfully:
                sys.exit()
            else:
                print("You pack up the rover with the help of Eugene.\n"
                      "All supplies loaded you prepare to drive to your first site.\n"
                      "-----------------\n\n")
                self.site_choice()

    def site_choice(self):
        choice = raw_input("Choose:\n"
                           "* ruby valley\n"
                           "* crimson lake\n"
                           "* scarlet rock\n\n")
        if "ruby" in choice:
            ruby = RubyValley(self)
            self.site_missions(ruby)
        elif "crimson" in choice:
            crimson = CrimsonLake(self)
            self.site_missions(crimson)
        elif "scarlet" in choice:
            scarlet = ScarletRock(self)
            self.site_missions(scarlet)
        else:
            self.site_choice()

    def site_missions(self, loc):
        choice = raw_input(loc.options)
        try:
            if 'rock' in choice:
                loc.gather_rocks()
            if 'plant' in choice:
                loc.plant_lichen()
            if 'explore' in choice:
                loc.explore()
            if 'go' in choice:
                loc.return_to_sites()
            if 'break' in choice:
                loc.take_break()
        except Exception:
            print ("can't do that\n")
        self.site_missions(loc)


class Being(object):
    def __init__(self, name):
        self.name = name


class Human(Being):
    def __init__(self, name):
        self.name = name
        self.hungry = True
        self.sleepy = False
        super(Human, self).__init__(self.name)


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
        self.speed = 1000                      # speed shuttle is moving at
        self.fuel = 100                        # perceent of fuel in shuttle
        self.structural_integrity = 100        # percent structural integrity left
        self.speed_alteration = 200            # rate at which speed changes
        self.fuel_usuage = 10                  # rate at which fuel is used
        self.distance = 10000                  # distance from surface
        self.landed_successfully = False       # shuttle landed successfully or not
        self.message = None                    # message to print out on landin

    def retroburn(self):
        """Not allowing negative speed, distance or fuel"""
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
            self.message = ("\nYou landed saftely but do not have enough fuel to return to Earth.\n"
                            "You plant the lichen and die watching strange stars dance.\n")
        elif self.structural_integrity <= 30:
            self.landed_successfully = False
            self.message = "\nYou hit the surface too fast and explode in a blaze of glory.\n"
        elif (self.structural_integrity > 30) and (self.structural_integrity < 80):
            self.landed_successfully = False
            self.message = ("\nYou hit the surface in a crumpled hull that no longer remotely resembles a shuttle.\n"
                            "You can no longer return to earth.\n"
                            "You plant the lichen and die watching strange stars dance.\n")
        else:
            self.landed_successfully = True
            self.message = "\nYou gracefully swoop down onto the red marshain surface with a perfect landing.\n"


class Location(object):
    def __init__(self, name, mission, options):
        self.name = name
        self.options = options
        self.mission = mission

    def return_to_sites(self):
        self.mission.site_choice()


class RubyValley(Location):
    def __init__(self, mission):
        self.planting_completed = False
        self.options = 'plant lichen\ngo to another site\n'
        self.msgs = {"plant": "\nYou planted lichen, one small step towards an atmosphere\n"}
        self.name = 'ruby'
        super(RubyValley, self).__init__(self.name, mission, self.options)

    def plant_lichen(self):
        print(self.msgs.get('plant'))
        self.planting_completed = True


class CrimsonLake(Location):
    def __init__(self, mission):
        self.options = 'explore\ngo to another site\n'
        self.msgs = {
            'explore': ("\nAfters hours of carful searching you find a small footprint fossilized in the ground,\n"
                        "it is a round paw with four circular toe indentations, you carefully chizel out the\n"
                        "fossilized foot print and place it in the spare rock container.\n"),
        }
        self.name = 'crimson'
        super(CrimsonLake, self).__init__(self.name, mission, self.options)

    def explore(self):
        print(self.msgs.get('explore'))


class ScarletRock(Location):
    def __init__(self, mission):
        self.options = 'gather rocks\ntake break\ngo to another site\n'
        self.msgs = {"rock": "\nYou gather serveral nice rock samples to be analyzed on earth\n",
                     "break": ("\nYou climb into the rover, seal in the pressure and take off your helmet.\n"
                               "You eat a satisfying lunch and admire the view as you snack on a candy bar.\n"
                               "You set down the candy bar to drink some water and when you look back\n"
                               "a little purple being is eating your candy bar!\n")}
        self.name = 'scarlet'
        self.rock_gathering = False
        super(ScarletRock, self).__init__(self.name, mission, self.options)

    def take_break(self):
        print(self.msgs.get("break"))
        self.final_first_choice()

    def gather_rocks(self):
        print(self.msgs.get('rock'))
        self.rock_gathering = True

    def final_first_choice(self):
        choice = raw_input(("* take back your candy bar\n"
                            "* say hi\n\n"))
        if "candy" in choice:
            print (("\nThe purple creature sadly hands you the candy bar and you eat the rest of it,\n"
                    "it's saliva poisons you and you die with the purple being looking very sad and worried.\n"))
            sys.exit()
        elif "hi" in choice:
            print("\nThe purple being eats the rest of the candy bar and then points towards a big rock ahead.\n")
            self.final_second_choice()
        else:
            self.final_first_choice()

    def final_second_choice(self):
        choice = raw_input(("* follow creature's point\n"
                            "* have eugene eliminate the creature\n\n"))
        if "follow" in choice:
            print(("\nThe rock disapears and you find you have driven into a street,\n"
                   "there is a whole city cloaked by a force field of sorts.\n"
                   "Putting your helmet on quickly as the purple creature tries to get out you \n"
                   "follow it outside and are surrounded by purple beings.\n"))
            self.final_third_choice()
        elif "eliminate" in choice:
            print(("\nYou return to earth with the alien body in the spare hibernation pod.\n"
                   "You are wildly popular but feel curious about that rock the rest of your life\n"))
            sys.exit()
        else:
            self.final_second_choice()

    def final_third_choice(self):
        choice = raw_input(("* take your picture with aliens\n"
                            "* try and capture an alien to take to earth\n"
                            "* say hello\n\n"))
        if "hello" in choice:
            print(("\nThe purple aliens wave at you as the purple alien that was with you runs into a\n"
                   "building and comes back out with a suitcase and points to the rover.\n"
                   "You get into the rover and wave goodbye to the aliens.\n"
                   "You drive back to the shuttle and get into the hibernation pods.\n"
                   "You and the alien arrive heros to earth, Splurp, the alien tours all the\n"
                   "great wonders of the world and then returns to mars on the next shuttle.\n"))
            sys.exit()
        if "picture" in choice:
            print("\nyou now have an awesome souvenier, way to go!\n")
        if "capture" in choice:
            print ("\nyou fail and are imprisoned, forever :(\n")
            sys.exit()
        else:
            self.final_third_choice()
