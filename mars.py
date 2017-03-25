import sys

class Shuttle(object):
	def __init__(self):
		self.speed = 1000 # speed shuttle is moving at
		self.fuel = 100 # percent of fuel in shuttle
		self.structural_integrity = 100 # percent structural integrity left
		self.speed_alteration = 200 # rate at which speed changes
		self.fuel_usage = 10 # rate at which fuel is used
		self.distance = 10000 # distance from surface

	def calc_landing_damage(self):
		if self.speed != 0:
			self.structural_integrity -= (self.speed * 0.1)

	# calculate distance change when `fall` is choosen
	def falling(self):
		if self.distance >= 2000:
			self.distance -= 2000
		else:
			self.distance = 0 # can't go below the surface!

	# calculate distance, fuel and speed changes when 'brake' is choosen
	def braking(self):
		"""Not allowing negative speed, distance or fuel"""
		if self.speed >= self.speed_alteration:
			self.speed -= self.speed_alteration
		else:
			self.speed = 0

		if self.fuel >= self.fuel_usage:
			self.fuel -= self.fuel_usage
		else:
			self.fuel = 0

		if self.distance >= 1000:
			self.distance -= 1000
		else:
			self.distance = 0

	# function for calculating if landing successful
	def calc_landing_success(self):
		if self.fuel < 60:
			print("You landed safely, but do not have enough fuel to return to Earth.\n\
			You die watching strange stars dance.")
			sys.exit() # this is a function built into python that tells the program to exit and stop running
		elif self.structural_integrity <= 30:
			print("You hit the surface too fast and explode in a blaze of glory.")
			sys.exit()
		elif (self.structural_integrity > 31) and (self.structural_integrity < 80):
			print("You hit the surface in a crumpled hull that no longer remotely resembles a shuttle.\n\
			You can no longer return to earth. You die watching strange stars dance.")
			sys.exit()
		else:
			print("Like a pro, you gracefully swoop down onto the red Martian surface with a perfect landing.")

	# main logic function
	def land_shuttle(self):
		while self.distance != 0:
			print("Shuttle distance from surface: {dist}, speed {speed}, fuel {fuel}".format(
			dist=self.distance, speed=self.speed, fuel=self.fuel))
			choice = raw_input("Type 'brake' to slow fall. Type 'fall' to continue falling.")

			if choice == "brake":
				self.braking()
			elif choice == "fall":
				self.falling()

		if self.distance == 0:
			self.calc_landing_damage()
			self.calc_landing_success()

print("Approaching mars")

astronaut_name = raw_input("Please type your name to start landing sequence.")

print("Astronaut {} selected to start shuttle landing sequence. Initiating release from main ship.".format(astronaut_name))

my_shuttle = Shuttle()
my_shuttle.land_shuttle()
