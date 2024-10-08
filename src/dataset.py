import random

# Dummy data dictionary of 30 Pokemon with their respective attacks
pokemon_attacks = {
    "Pikachu": "Thunderbolt",
    "Charizard": "Flamethrower",
    "Bulbasaur": "Vine Whip",
    "Squirtle": "Water Gun",
    "Jigglypuff": "Sing",
    "Meowth": "Scratch",
    "Psyduck": "Confusion",
    "Machop": "Karate Chop",
    "Geodude": "Rock Throw",
    "Ponyta": "Ember",
    "Magnemite": "Thunder Shock",
    "Gastly": "Lick",
    "Onix": "Rock Slide",
    "Cubone": "Bone Club",
    "Hitmonlee": "High Jump Kick",
    "Koffing": "Sludge",
    "Rhyhorn": "Horn Attack",
    "Horsea": "Bubble",
    "Staryu": "Water Pulse",
    "Scyther": "Slash",
    "Electabuzz": "Thunder Punch",
    "Magmar": "Fire Punch",
    "Pinsir": "Vice Grip",
    "Tauros": "Tackle",
    "Gyarados": "Hydro Pump",
    "Lapras": "Ice Beam",
    "Eevee": "Quick Attack",
    "Snorlax": "Body Slam",
    "Articuno": "Blizzard",
    "Zapdos": "Drill Peck",
}


def random_pokemon_attack():
    pokemon, attack = random.choice(list(pokemon_attacks.items()))
    print(f"{pokemon} used {attack} and it was super effective!")


# Generate a random Pokemon attack
random_pokemon_attack()
