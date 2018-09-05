class Vehicle(object):
    def __init__(self, vehicle_type, number_of_wheels):
        self.vehicle_type = vehicle_type
        self.number_of_wheels = number_of_wheels

    def vehicle_type(self):
        return self.vehicle_type

    #def number_of_wheels(self):
        #return self.number_of_wheels

    def number_of_wheels(self, number):
        self.number_of_wheels = number

    def vehicle_type(self, vehicle_type_p):
        self.vehicle_type = vehicle_type_p


Subaru = Vehicle('Subaru', 4)
print(Subaru.number_of_wheels)
