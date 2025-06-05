# Task: Inheritance and Polymorphism - Extend Car into ElectricCar

# ✅ Inheritance:
# Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class).
# It helps in code reuse and creating hierarchical relationships.

# ✅ Polymorphism:
# Polymorphism allows different classes to define methods with the same name but different behavior.
# In this example, both Car and ElectricCar have their own versions of display() and start_engine().

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


# ElectricCar is a child class that inherits from the Car class
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        # Call the parent constructor using super()
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity  # in kWh

    # Polymorphism: Overriding the display method
    def display(self):
        super().display()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

    # Polymorphism: Overriding the start_engine method
    def start_engine(self):
        print(f"{self.make} {self.model} powers up silently ⚡🔋")
        print("Zooming ahead...🔌🚘")


# Example usage
my_ecar = ElectricCar("Tesla", "Model 3", 2023, "White", 75)
my_ecar.display()
my_ecar.start_engine()
