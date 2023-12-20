import random

# TODO Handle Secret characters
# TODO Handle DLC weapons
# TODO Add ability to pick a random map for a run

# All characters including DLC (skipping Ghost because it doesn't deal damage)
all_characters = ["Antonio", "Imelda", "Pasqualina", "Gennaro", "Arca", "Porta", "Lama", "Poe", "Clerici", "Dommario", "Krochi", "Christine", "Pugnala" , "Giovanna", "Poppea", "Concetta", "Mortaccio",
                    "Cavallo", "Ramba", "O'Sole", "Ambrojoe", "Gallo", "Divano", "Zi'Assunta", "Sigma", "She-Moon", "Miang", "Menya", "Syuuto", "Babi-Onna", "McCoy-Oni" , "Menya", "Syuuto", 
                    "Gav'Et-Oni", "Eleanor", "Maruto", "Keitha", "Luminaire", "Genevieve", "Je-Ne-Viv", "Sammy", "Rottin'Ghoul", "Crewmate", "Engineer", "Shapeshifter", "Guardian", "Imposter",
                    "Scientist", "Horse", "Imposter"]



# List of weapons in base game
base_game_weapons = ["Whip", "Magic Wand", "Knife", "Axe", "Cross", "King Bible", "Fire Wand", "Garlic", "Santa Water", "Rune Tracer", "Lightning Ring" "Pentagram", "Peachone", "Ebony Wings", "Phiera Der Tuphello",
            "Eight The Sparrow", "Gatti Amari", "Song of Mana", "Shadow Pinion", "Clock Lancet", "Laurel", "Vento Sacro", "Bone", "Cherry Bomb", "Carrello", "Celestial Dusting", "La Robba", "Greatest Jubillee",
            "Bracelet", "Candybox", "Victory Sword", "Flame of Misspell", "Glass Fandango"]

# List of passive items in Vampire Survivors
passive_items = ["Spinach", "Armor", "Hollow Heart", "Pummarola", "Empty Tome", "Candelabrador", "Bracer", "Spellbinder", "Duplicator", "Wings", "Attractorb", "Clover", "Crown", "Stone Mask", "Tiragisu", "Torrona's Box"]

def generate_random_build():
    character = random.choice(all_characters)
    weapon = random.sample(base_game_weapons, 6)
    passive_item = random.sample(passive_items, 6)

    return f"Character: {character}\nWeapon: {weapon}\nPassive Item: {passive_item}"

# Generate and print a random build
print(generate_random_build())
