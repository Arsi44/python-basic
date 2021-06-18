class Vehicle():
    def __init__(self, vehicle_type, weight, lifting_capacity):
        self.vehicle_type = vehicle_type
        self.weight = weight
        self.lifting_capacity = lifting_capacity

    def honking(self):
        print('Honking by', self.vehicle_type)


class Plane(Vehicle):

    def __init__(self, *args, wing_count, **kwargs):
        super().__init__(*args, **kwargs)
        self.wing_count = wing_count

    def honking(self):
        print('Unavailabele to honking by', self.vehicle_type)


if __name__ == '__main__':
    p = Plane(2, 3, 4, wing_count=5)
    print(dir(p))
