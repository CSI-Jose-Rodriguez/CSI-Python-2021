import math

# gun = "DVL-10"
# caliber = "7.62x51mm NATO"
# ammunition = "7.62x51mm M80"
# velocity_ms = 833

# building = "Soleil"
# buildingHeight = 288

# gravity_ms = 9.81

def ProjectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms:int, building:str, buildingHeight:int, gravity_ms:int):
    time_s = math.sqrt((2 * buildingHeight) / gravity_ms)
    
    distance_m = (velocity_ms * time_s)

    print(f"The gun slected for the experiment is {gun}. Its claiber is {caliber} and uses {ammunition} as its ammunition. It shoots at a velocity of {velocity_ms}m/s. It is being shot from {building} that is {buildingHeight} feet above the ground.")


ProjectileFunction("DVL-10", "7.62x51mm NATO", "7.62x51mm M80", 833, "Soleil", 288, 9.81)