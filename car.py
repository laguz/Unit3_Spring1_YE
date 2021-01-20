
class vehicle():
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("We are Driving", self.model)

    def advertise(self):
        print("Buy OUR", self.model)


class SUV(vehicle):
    def __init__(self, make, model, year, color, num_wheels):
        super().__init__(make, model, year, color)
        self.num_wheels = num_wheels

    def advertise(self):
        print("Buy OUR SUV , ", self.model)


class Sedan(vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)

    def advertise(self):
        print("Buy OUR Fantastic roomy %s for less" % self.make)

if __name__ == "__main__":
    # sedan = vehicle ("Toyota", "Rav4", 2020, "Gray")
    # sedan.drive()
    # sedan.advertise()
    sedan2 = Sedan("Toyota", "Rav4", 2016, "Gray")
    sedan2.advertise()
    print(sedan2.make)
