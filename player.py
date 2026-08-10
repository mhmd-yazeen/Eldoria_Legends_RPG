# player.py
import time
from config import CLASSES, WEAPONS_POOL, ARMOR_POOL, POTIONS_POOL
from utils import print_header, get_input

player = {
    "name": "",
    "class": "",
    "level": 1,
    "exp": 0,
    "max_exp": 100,
    "hp": 100,
    "max_hp": 100,
    "mana": 50,
    "max_mana": 50,
    "atk": 15,
    "def": 5,
    "crit": 0.05,
    "gold": 100,
    "weapon": None,
    "armor": None,
    "inventory": [],
    "bosses_defeated": 0,
    "enemies_defeated": 0,
    "weapons_collected": 0,
    "rare_items_found": 0,
    "start_time": 0,
}


def create_character():
    print_header("CHARACTER CREATION")
    name = input("Enter Player Name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter Player Name: ").strip()

    print("\nChoose Your Class:")
    print("1. Warrior   (High HP/Def, Low Mana)")
    print("2. Mage      (High Mana/Atk, Low Def)")
    print("3. Archer    (Balanced, High Crit)")
    print("4. Assassin  (High Atk/Crit, Low HP)")

    choice = get_input("Select Class (1-4): ", ["1", "2", "3", "4"])
    class_names = ["Warrior", "Mage", "Archer", "Assassin"]
    selected_class = class_names[int(choice) - 1]

    base = CLASSES[selected_class]
    player["name"] = name
    player["class"] = selected_class
    player["hp"] = base["hp"]
    player["max_hp"] = base["max_hp"]
    player["mana"] = base["mana"]
    player["max_mana"] = base["max_mana"]
    player["atk"] = base["atk"]
    player["def"] = base["def"]
    player["crit"] = base["crit"]
    player["start_time"] = time.time()

    player["weapon"] = WEAPONS_POOL[0]  # Wooden Sword
    player["armor"] = ARMOR_POOL[0]    # Cloth Tunic
    player["inventory"].append(POTIONS_POOL[0].copy())
    player["inventory"].append(POTIONS_POOL[5].copy())

    print(f"\nWelcome, {name} the {selected_class}! Your journey begins in Eldoria.")


def view_stats():
    print_header("PLAYER STATS")
    w_dmg = player["weapon"]["dmg"] if player["weapon"] else 0
    a_def = player["armor"]["def"] if player["armor"] else 0
    a_hp = player["armor"]["hp"] if player["armor"] else 0
    a_mana = player["armor"]["mana"] if player["armor"] else 0

    print(f"Name: {player['name']} | Class: {player['class']}")
    print(f"Level: {player['level']} | EXP: {player['exp']}/{player['max_exp']}")
    print(f"HP: {player['hp']}/{player['max_hp'] + a_hp} | Mana: {player['mana']}/{player['max_mana'] + a_mana}")
    print(f"Attack: {player['atk']} (+{w_dmg}) | Defense: {player['def']} (+{a_def})")
    print(f"Critical Chance: {int((player['crit'] + (player['weapon']['crit_bonus'] if player['weapon'] else 0))*100)}%")
    print(f"Gold: {player['gold']}")
    print(f"Weapon: {player['weapon']['name'] if player['weapon'] else 'None'}")
    print(f"Armor: {player['armor']['name'] if player['armor'] else 'None'}")
    print(f"Bosses Defeated: {player['bosses_defeated']}/10")


def level_up_check():
    while player["exp"] >= player["max_exp"] and player["level"] < 100:
        current_cap = (player["bosses_defeated"] + 1) * 10
        if player["level"] >= current_cap:
            print(f"\n[Cap Reached] Defeat the Level {current_cap} Boss to continue leveling!")
            player["exp"] = player["max_exp"] - 1
            break

        player["exp"] -= player["max_exp"]
        player["level"] += 1
        player["max_exp"] = int(player["max_exp"] * 1.25)

        player["max_hp"] += 20
        player["max_mana"] += 10
        player["atk"] += 4
        player["def"] += 2
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]

        print(f"\nLEVEL UP! You reached Level {player['level']}! All stats increased and resources fully restored!")