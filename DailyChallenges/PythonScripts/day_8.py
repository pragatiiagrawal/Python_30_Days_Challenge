# Task: Create a car class with attributes and display method 
class Car:
    def __init__(self, make, model, year, color):
        # Initialize the car attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        # Display the car details
        print("Car Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

    def start_engine(self):
        # Simulate starting the engine
        print(f"{self.make} {self.model} engine started!🔥")
        print("Ready to roll!!...🚗")

# Example usage
my_car = Car("Lamborghini", "Huracán", 2014, "Red")
my_car.display()
my_car.start_engine()
