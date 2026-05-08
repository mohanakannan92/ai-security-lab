import random
from attack_dataset import ATTACK_DATASET


def generate_attack(category=None):
    """
    Generate a random attack.
    If category provided → pick from that category
    """

    if category:
        attacks = ATTACK_DATASET.get(category, [])
        return random.choice(attacks) if attacks else None

    # Random category
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
        attacks.append(attack)

    return attacks