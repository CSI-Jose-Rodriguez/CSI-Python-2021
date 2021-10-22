print("Welcome to Simpsons' Shipping")

weight = float(input("What is the weight of your package:"))

#ground shipping
if (weight <= 2):
    cost_ground = weight * 1.75 + 20
    print("Ground Shipping: $", float(cost_ground))
elif (weight <= 6 and weight > 2):
    cost_ground = weight * 3.50 + 20
    print("Ground Shipping: $", float(cost_ground))
elif (weight <= 10 and weight > 6):
    cost_ground = weight * 4.50 + 20
    print("Ground Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 5.25 + 20
    print("Ground Shipping: $", float(cost_ground))

#courier shipping
if (weight <= 2):
    cost_courier = weight * 3.50 + 5.00
    print("Courier Shipping: $", float(cost_courier))
elif (weight <= 6 and weight > 2):
    cost_courier = weight * 7.00 + 8.00
    print("Courier Shipping: $", float(cost_courier))
elif (weight <= 10 and weight > 6):
    cost_courier = weight * 9.00 + 12.00
    print("Courier Shipping: $", float(cost_courier))
else:
    cost_courier = weight * 10.50 + 15.00
    print("Courier Shipping: $", float(cost_courier))

#drone shipping
if (weight <= 2):
    cost_drone = weight * 5.25
    print("Drone Shipping: $", float(cost_drone))
elif (weight <= 6 and weight > 2):
    cost_drone = weight * 10.50
    print("Drone Shipping: $", float(cost_drone))
elif (weight <= 10 and weight > 6):
    cost_drone = weight * 13.50
    print("Drone Shipping: $", float(cost_drone))
else:
    cost_drone = weight * 15.75
    print("Drone Shipping: $", float(cost_drone))

#ground shipping premium
print("Ground Premium Shipping: $150")