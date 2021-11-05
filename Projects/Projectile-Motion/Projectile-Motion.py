import math
from ExperimentalData import ExperimentalData

# gun = "DVL-10"
# caliber = "7.62x51mm NATO"
# ammunition = "7.62x51mm M80"
# velocity_ms = 833

# building = "Soleil"
# buildingHeight = 288

# gravity_ms = 9.81

def ProjectileFunction(experimentalData: ExperimentalData):
    time_s = math.sqrt((2 * experimentalData.buildingHeight) / experimentalData.gravity_ms)
    
    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)

    print(f"The gun slected for the experiment is {experimentalData.gun}. Its claiber is {experimentalData.caliber} and uses {experimentalData.ammunition} as its ammunition. It shoots at a velocity of {experimentalData.velocity_ms}m/s. It is being shot from {experimentalData.building} that is {experimentalData.buildingHeight} feet above the ground.")

# experimentalData = {

# "gun": "DVL-10",
# "caliber": "7.62x51mm NATO",
# "ammunition": "7.62x51mm M80",
# "velocity_ms": 833,
# "building": "Soleil",
# "buildingHeight": 288,
# "gravity_ms": 9.81

# }

experimentalData = ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm M80", 833, "Soleil", 288, 9.81)

ProjectileFunction