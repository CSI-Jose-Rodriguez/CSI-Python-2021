import random

name =input("What is your name?\n")
print(f"Hello {name}! Welcome to Magic 8 Ball")
question =input("What do you want to ask me?\n")
print(f"{name} ask: {question}")

random_number = random.randint(1, 12)
if (random_number == 1):
    print("Yes - definitely.")
elif (random_number == 2):
    print("It is decidedly so.")
elif (random_number == 3):
    print("Without a doubt.")
elif (random_number == 4):
    print("Reply hazy, try again.")
elif (random_number == 5):
    print("Ask again later")
elif (random_number == 6):
    print("Better not tell you now.")
elif (random_number == 7):
    print("My sources say NO.")
elif (random_number == 8):
    print("Outlook not so good.")
elif (random_number == 9):
    print("Very doubtful.")
elif (random_number == 10):
    print("100%.")
elif (random_number == 11):
    print("LOL no.")
elif (random_number == 12):
    print("You wish.")