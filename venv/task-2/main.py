class Vehicle():
    def __init__(self, vehicle_type, weight, lifting_capacity):
        self.vehicle_type = vehicle_type
        self.weight = weight
        self.lifting_capacity = lifting_capacity

    def honking(self):
        print('Honking by', self.vehicle_type)


class Plane(Vehicle):
    def honking(self):
        print('Unavailabele to honking by', self.vehicle_type)
