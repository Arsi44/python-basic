from dataclasses import dataclass


@dataclass()
class Vehicle:
    vehicle_type: str
    weight: int
    lifting_capacity: int

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
