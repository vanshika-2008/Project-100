class Car(object) :
    def __init__(self, colour, company, maximum, model) :
        self.colour = colour
        self.company = company
        self.speedmax = maximum
        self.model = model

    def start(self) :
        print("The car is started")

    def stop(self) :
        print("The car is stopped")

Verna = Car("black", "Hyundai", "240", "Luxury")
print(Verna.colour)
Verna.start()