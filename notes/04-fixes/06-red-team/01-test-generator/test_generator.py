# Import dataset directly (for unique selection)
from attack_dataset import ATTACK_DATASET
import random

# How many attacks you want
NUM_ATTACKS = 10

# Step 1: Combine all attacks into one list
all_attacks = []

for category, attacks in ATTACK_DATASET.items():
    for attack in attacks:
        all_attacks.append({
            "category": category,
            "attack": attack
        })

# Step 2: Pick unique attacks (no duplicates)
selected_attacks = random.sample(all_attacks, NUM_ATTACKS)

# Step 3: Print results
for i, attack in enumerate(selected_attacks, 1):
    print(f"{i}. [{attack['category']}] {attack['attack']}")