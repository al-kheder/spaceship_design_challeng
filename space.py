#Base Spaceship
class Spaceship:
    def __init__(self, name, fuel_capacity, speed):
        self.name = name
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity
        self.speed = speed
        self.status = "Docked"


    def launch(self):
        if self.current_fuel > 0:
            self.status = "In Flight"
            print(f"{self.name} has launched!")
        else:
            print(f"{self.name} cannot launch: out of fuel.")

    def land(self):
        self.status = "Docked"
        print(f"{self.name} has landed.")

    def refuel(self, amount):
        if self.current_fuel + amount <= self.fuel_capacity:
            self.current_fuel += amount
            print(f"{self.name} has been refueled. Current fuel: {self.current_fuel}")
        else:
            print(f"Cannot refuel {self.name}: fuel capacity exceeded.")

    def check_status(self):
        return f"{self.name} Status: {self.status}, Fuel: {self.current_fuel}/{self.fuel_capacity}, Speed: {self.speed}"


#Commercial Spaceship 🏢
class CommercialSpaceship(Spaceship):
    def __init__(self, name, fuel_capacity, speed, passenger_capacity, entertainment_system):
        super().__init__(name, fuel_capacity, speed)
        self.passenger_capacity = passenger_capacity
        self.entertainment_system = entertainment_system

    def serve_food(self):
        if self.entertainment_system:
            print(f"{self.name} is serving food to passengers.")
        else:
            print(f"{self.name} does not have an entertainment system to serve food.")



#Research Spaceship   🔬
class ResearchSpaceship(Spaceship):
    def __init__(self, name, fuel_capacity, speed, lab_equipment):
        super().__init__(name, fuel_capacity, speed)
        self.lab_equipment = lab_equipment

    def conduct_experiment(self, experiment_name):
        print(f"{self.name} is conducting experiment: {experiment_name}.")



#Exploration Spaceship 🌌
class ExplorationSpaceship(Spaceship):
    def __init__(self, name, fuel_capacity, speed, exploration_range):
        super().__init__(name, fuel_capacity, speed)
        self.exploration_range = exploration_range

    def scan_planet(self, planet_name):
        print(f"{self.name} is scanning planet: {planet_name}.")



# Create instances of each spaceship
commercial_ship = CommercialSpaceship("Galactic Voyager", 1000, 50000, 200, True)
research_ship = ResearchSpaceship("Stellar Explorer", 1500, 40000, ["Microscope", "Spectrometer"])
exploration_ship = ExplorationSpaceship("Cosmic Pioneer", 2000, 60000, 1000000)

# Test functionality
commercial_ship.launch()
commercial_ship.serve_food()
print(10 * " * ")
research_ship.land()
research_ship.conduct_experiment("Microgravity Study")
print(10 * " * ")

exploration_ship.refuel(500)
exploration_ship.scan_planet("Mars")

# Check status of all spaceships
print(commercial_ship.check_status())
print(research_ship.check_status())
print(exploration_ship.check_status())