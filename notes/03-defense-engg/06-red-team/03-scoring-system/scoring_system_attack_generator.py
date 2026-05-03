import random
from attack_dataset import ATTACK_DATASET


def generate_attack(category=None):
    """
    Generate a random attack.
    If category is provided → pick from that category
    """

    # If specific category requested
    if category:
        attacks = ATTACK_DATASET.get(category, [])

        if not attacks:
            return None

        return {
            "category": category,
            "attack": random.choice(attacks)
        }

    # Pick random category
    category = random.choice(list(ATTACK_DATASET.keys()))
    attack = random.choice(ATTACK_DATASET[category])

    return {
        "category": category,
        "attack": attack
    }


def generate_bulk_attacks(n=10):
    """
    Generate multiple attacks
    """

    attacks = []

    for _ in range(n):
        attack = generate_attack()

        # Skip if None (safety check)
        if attack:
            attacks.append(attack)

    return attacks