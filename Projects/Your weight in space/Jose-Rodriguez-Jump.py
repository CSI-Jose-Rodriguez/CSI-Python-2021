planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity =[2.56, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Jumping on other plantes")
myJump = float(input("What is your jump on Earth (meters)? "))

myPlanet = input(f"Select a planet from the list: {planets}\n")
def calculateJump(planet, jump):
    print(f"Your jump in Earth is: {jump}")

    planet_index = planets.index(planet)
    print(f"Your jump in {planets[planet_index]} is  {(jump * rel_gravity[planet_index])} meters. ")

calculateJump(myPlanet, myJump)