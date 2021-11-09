import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json

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

    print(f"The gun slected for the experiment is {experimentalData.gun}. Its claiber is {experimentalData.caliber} and uses {experimentalData.ammunition} as its ammunition. It shoots at a velocity of {experimentalData.velocity_ms}m/s. It is being shot from {experimentalData.building} that is {experimentalData.buildingHeight} feet above the ground. The distance to the target is {distance_m} meters. It would take {time_s} seconds to reach it.")

# experimentalData = {

# "gun": "DVL-10",
# "caliber": "7.62x51mm NATO",
# "ammunition": "7.62x51mm M80",
# "velocity_ms": 833,
# "building": "Soleil",
# "buildingHeight": 288,
# "gravity_ms": 9.81

# }

# experimentalData = ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm M80", 833, "Soleil", 288, 9.81)


myDataSet = [
ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm M80", 833, "Soleil", 288, 9.81),
ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Popular Center", 247, 9.81),
ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm M62", 816, "Caribbean Sea View", 334, 9.81),
ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm BCP FMJ", 840, "Coliseum Tower Residences", 259, 9.81),
ExperimentalData("DVL-10", "7.62x51mm NATO", "7.62x51mm M993", 910, "Aquablue 2", 279, 9.81)

]

for data in myDataSet:
    print("\n-------------------------------------------------------\n")
    ProjectileFunction(data)

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)