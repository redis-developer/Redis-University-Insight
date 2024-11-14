import random
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
cmds = []

# Define base data
brands = ["Speedster", "Zoomer", "WindRider", "FlashBike", "RoadMaster"]
types = ["Road", "Mountain", "Hybrid", "Electric", "Touring"]
materials = ["carbon fiber", "aluminum", "steel", "titanium"]
descriptions = {
    "Road": "The Racer is built for speed and performance on the road!",
    "Mountain": "Designed for rugged terrain and off-road adventures.",
    "Hybrid": "Combines the best features of road and mountain bikes.",
    "Electric": "Assisted pedaling for an effortless ride.",
    "Touring": "Perfect for long journeys with comfort and durability."
}
addons_list = [["water bottle holder", "bike lock"], ["kickstand", "bell"], ["bike rack", "fenders"], ["GPS tracker", "phone mount"]]


# Function to generate a random bicycle entry
def generate_bike():
    brand = random.choice(brands)
    bike_type = random.choice(types)
    price = round(random.uniform(300, 1500), 2)
    material = random.choice(materials)
    weight = round(random.uniform(7, 15), 1)
    description = descriptions[bike_type]
    addons = random.choice(addons_list)
    helmet_included = random.choice([True, False])
    condition = "new" if random.random() > 0.2 else "used"
    
    return {
        "brand": brand,
        "price": price,
        "type": bike_type,
        "specs": {
            "material": material,
            "weight": weight
        },
        "description": description,
        "addons": addons,
        "helmet_included": helmet_included,
        "condition": condition
    }

# Generate 500,000 bikes
bikes = [generate_bike() for _ in range(500000)]

for i in range(500000):
    cmd = "JSON.SET " + f"bike:{i+1} " + "$ " + "'" + json.dumps(bikes[i]) + "'"
    cmds.append(cmd)

with open("add_bikes.txt", "w") as file:
    for cmd in cmds:
        file.write(str(cmd).strip('()') + "\n")