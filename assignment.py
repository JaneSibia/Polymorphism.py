class Vehicle:
    def __init__(self, type, brand, model):
        self.type = type
        self.brand = brand
        self.model = model

    def move(self):
        print(f"The {self.type} is moving.")

    def display_info(self):
        print(f"""
        Type: {self.type}
        Brand: {self.brand}
        Model: {self.model}
        """)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__("Car", brand, model)
        self.fuel_type = fuel_type
        self.current_gear = "P"

    def move(self):
        if self.current_gear == "P":
            print("🚗 Can't move - car is in Park!")
            return
        print(f"🚗 {self.brand} {self.model} is driving on {self.fuel_type} fuel.")

    def shift_gear(self, gear):
        valid_gears = ["P", "R", "N", "D"]
        if gear in valid_gears:
            self.current_gear = gear
            print(f"Shifted to {gear}")
        else:
            print("Invalid gear!")


class Plane(Vehicle):
    def __init__(self, brand, model, airline):
        super().__init__("Plane", brand, model)
        self.airline = airline
        self.is_flying = False

    def move(self):
        if not self.is_flying:
            print("✈️ Plane must take off before flying!")
            return
        print(f"✈️ {self.airline} {self.brand} {self.model} is cruising at 35,000 feet.")

    def take_off(self):
        self.is_flying = True
        print(f"✈️ {self.brand} {self.model} is taking off!")

    def land(self):
        self.is_flying = False
        print(f"✈️ {self.brand} {self.model} has landed safely.")


class Bicycle(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__("Bicycle", brand, model)
        self.bike_type = bike_type
        self.is_pedaling = False

    def move(self):
        if not self.is_pedaling:
            print("🚲 You need to pedal to move the bicycle!")
            return
        print(f"🚲 {self.brand} {self.model} {self.bike_type} bike is moving.")

    def pedal(self):
        self.is_pedaling = True
        print("🚲 Pedaling started...")

    def brake(self):
        self.is_pedaling = False
        print("🚲 Applying brakes...")


# Demonstrate polymorphism
vehicles = [
    Car("Toyota", "Camry", "gasoline"),
    Plane("Boeing", "747", "Delta"),
    Bicycle("Trek", "FX 2", "hybrid")
]

# Set up each vehicle properly
vehicles[0].shift_gear("D")  # Put car in Drive
vehicles[1].take_off()       # Plane takes off
vehicles[2].pedal()          # Start pedaling bike

# All vehicles move differently
for vehicle in vehicles:
    vehicle.display_info()
    vehicle.move()
    print("-------------------")