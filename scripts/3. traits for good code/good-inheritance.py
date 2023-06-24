class Vehicle:
    def __init__(self, color, weight, speed):
        self.color = color
        self.weight = weight
        self.speed = speed

    def start(self):
        print("starting...")

    def stop(self):
        print("stoping...")

    def accelerate(self):
        print("acceleratinhg...")


class Car(Vehicle):
    def __init__(self, color, weight, speed, num_doors):
        super().__init__(color, weight, speed)
        self.num_doors = num_doors

    def honk(self):
        print("honking")


if __name__ == "__main__":
    car = Car("Black", 12, 300, 6)
    car.accelerate()
