# print("Good Evening Globe")
# print("What is thy calling?")
# myName = input()
# print("It is splendid to meet you" , myName)
# print("The extent of thy calling is: " , len(myName))
# print("What is thy time spent alive?")
# myAge = input()
# print("You will accomplish " + str(int(myAge) + 5) + " in 5 rotations")

print("Force Calculator")
print("""             -----------
             |
             | 
             |-----
             |
             |                         """)
mass = int(input("What is the mass?: "))
acceleration = int(input("What is the acceleration?: "))
print("The force is: ", str(int(mass) * int(acceleration)) + " Newton")

print("Force Calculator")
print("""             -----------
             |
             | 
             |-----
             |
             |                         """)
def Force(mass, acceleration):  
    print(f"Force is {int(mass) * int(acceleration)}")
print("Mass is 80")
print("acceleration is 90")
Force(80, 90)