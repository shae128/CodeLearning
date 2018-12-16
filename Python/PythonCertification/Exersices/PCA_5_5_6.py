class Vehicle:
	pass


class LandVehicle(Vehicle):
	pass


class TrackedVehicle(LandVehicle):
	pass


for cl1 in [Vehicle, LandVehicle, TrackedVehicle]:
	for cl2 in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(cl1,cl2),end='\t')
	print()
