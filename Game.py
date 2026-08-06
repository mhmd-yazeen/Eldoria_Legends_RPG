import json
import os
import random
import sys
import time

# =====================================================================
# DATA CONFIGURATIONS & TABLES
# =====================================================================

CLASSES = {
    "Warrior": {
        "hp": 150,
        "max_hp": 150,
        "mana": 40,
        "max_mana": 40,
        "atk": 18,
        "def": 12,
        "crit": 0.05,
        "skills": {
            "Slash": {"cost": 5, "multiplier": 1.2, "type": "damage"},
            "Shield Bash": {"cost": 10, "multiplier": 1.4, "type": "damage"},
            "Rage": {"cost": 15, "multiplier": 1.8, "type": "damage"},
            "Earthquake": {"cost": 25, "multiplier": 2.5, "type": "damage"},
        },
    },
    "Mage": {
        "hp": 100,
        "max_hp": 100,
        "mana": 100,
        "max_mana": 100,
        "atk": 22,
        "def": 5,
        "crit": 0.10,
        "skills": {
            "Fireball": {"cost": 10, "multiplier": 1.3, "type": "damage"},
            "Ice Blast": {"cost": 20, "multiplier": 1.6, "type": "damage"},
            "Thunder Strike": {"cost": 30, "multiplier": 2.0, "type": "damage"},
            "Meteor": {"cost": 50, "multiplier": 3.0, "type": "damage"},
        },
    },
    "Archer": {
        "hp": 120,
        "max_hp": 120,
        "mana": 60,
        "max_mana": 60,
        "atk": 16,
        "def": 8,
        "crit": 0.20,
        "skills": {
            "Multi Shot": {"cost": 10, "multiplier": 1.2, "type": "damage"},
            "Poison Arrow": {"cost": 15, "multiplier": 1.5, "type": "damage"},
            "Explosive Arrow": {"cost": 25, "multiplier": 2.0, "type": "damage"},
            "Sniper Shot": {"cost": 40, "multiplier": 2.8, "type": "damage"},
        },
    },
    "Assassin": {
        "hp": 90,
        "max_hp": 90,
        "mana": 50,
        "max_mana": 50,
        "atk": 20,
        "def": 6,
        "crit": 0.35,
        "skills": {
            "Backstab": {"cost": 10, "multiplier": 1.4, "type": "damage"},
            "Smoke Bomb": {"cost": 15, "multiplier": 1.1, "type": "damage"},
            "Shadow Strike": {"cost": 25, "multiplier": 2.2, "type": "damage"},
            "Instant Kill": {"cost": 45, "multiplier": 4.0, "type": "damage"},
        },
    },
}

WEAPONS_POOL = [
    # Common (x1.0, +0%)
    {
        "name": "Wooden Sword",
        "rank": "Common",
        "dmg": 5,
        "crit_bonus": 0.00,
        "price": 20,
        "req_lvl": 1,
    },
    {
        "name": "Rusty Axe",
        "rank": "Common",
        "dmg": 6,
        "crit_bonus": 0.00,
        "price": 25,
        "req_lvl": 1,
    },
    {
        "name": "Training Bow",
        "rank": "Common",
        "dmg": 4,
        "crit_bonus": 0.00,
        "price": 18,
        "req_lvl": 1,
    },
    # Uncommon (x1.1, +2%)
    {
        "name": "Bronze Dagger",
        "rank": "Uncommon",
        "dmg": 10,
        "crit_bonus": 0.02,
        "price": 50,
        "req_lvl": 5,
    },
    {
        "name": "Apprentice Staff",
        "rank": "Uncommon",
        "dmg": 12,
        "crit_bonus": 0.02,
        "price": 60,
        "req_lvl": 5,
    },
    {
        "name": "Hunting Bow",
        "rank": "Uncommon",
        "dmg": 11,
        "crit_bonus": 0.02,
        "price": 55,
        "req_lvl": 5,
    },
    # Rare (x1.3, +5%)
    {
        "name": "Iron Sword",
        "rank": "Rare",
        "dmg": 20,
        "crit_bonus": 0.05,
        "price": 120,
        "req_lvl": 10,
    },
    {
        "name": "Steel Axe",
        "rank": "Rare",
        "dmg": 24,
        "crit_bonus": 0.05,
        "price": 150,
        "req_lvl": 12,
    },
    {
        "name": "Long Bow",
        "rank": "Rare",
        "dmg": 22,
        "crit_bonus": 0.05,
        "price": 135,
        "req_lvl": 11,
    },
    # Super Rare (x1.5, +8%)
    {
        "name": "Crystal Blade",
        "rank": "Super Rare",
        "dmg": 38,
        "crit_bonus": 0.08,
        "price": 300,
        "req_lvl": 20,
    },
    {
        "name": "Shadow Dagger",
        "rank": "Super Rare",
        "dmg": 35,
        "crit_bonus": 0.08,
        "price": 280,
        "req_lvl": 20,
    },
    {
        "name": "Lightning Bow",
        "rank": "Super Rare",
        "dmg": 40,
        "crit_bonus": 0.08,
        "price": 320,
        "req_lvl": 22,
    },
    # Epic (x1.8, +12%)
    {
        "name": "Flame Sword",
        "rank": "Epic",
        "dmg": 65,
        "crit_bonus": 0.12,
        "price": 700,
        "req_lvl": 35,
    },
    {
        "name": "Ice Spear",
        "rank": "Epic",
        "dmg": 68,
        "crit_bonus": 0.12,
        "price": 750,
        "req_lvl": 38,
    },
    {
        "name": "Thunder Hammer",
        "rank": "Epic",
        "dmg": 72,
        "crit_bonus": 0.12,
        "price": 800,
        "req_lvl": 40,
    },
    # Mythical (x2.2, +18%)
    {
        "name": "Phoenix Blade",
        "rank": "Mythical",
        "dmg": 110,
        "crit_bonus": 0.18,
        "price": 1500,
        "req_lvl": 55,
    },
    {
        "name": "Demon Slayer",
        "rank": "Mythical",
        "dmg": 120,
        "crit_bonus": 0.18,
        "price": 1800,
        "req_lvl": 60,
    },
    {
        "name": "Celestial Staff",
        "rank": "Mythical",
        "dmg": 115,
        "crit_bonus": 0.18,
        "price": 1650,
        "req_lvl": 58,
    },
    # Legendary (x2.8, +25%)
    {
        "name": "Dragon King's Sword",
        "rank": "Legendary",
        "dmg": 200,
        "crit_bonus": 0.25,
        "price": 4000,
        "req_lvl": 80,
    },
    {
        "name": "Blade of Eternity",
        "rank": "Legendary",
        "dmg": 220,
        "crit_bonus": 0.25,
        "price": 5000,
        "req_lvl": 85,
    },
    {
        "name": "Bow of the Gods",
        "rank": "Legendary",
        "dmg": 210,
        "crit_bonus": 0.25,
        "price": 4500,
        "req_lvl": 82,
    },
]

ARMOR_POOL = [
    # Common
    {
        "name": "Cloth Tunic",
        "rank": "Common",
        "def": 3,
        "hp": 10,
        "mana": 5,
        "crit_res": 0.01,
        "price": 20,
    },
    {
        "name": "Leather Vest",
        "rank": "Common",
        "def": 5,
        "hp": 15,
        "mana": 0,
        "crit_res": 0.01,
        "price": 30,
    },
    # Uncommon
    {
        "name": "Padded Armor",
        "rank": "Uncommon",
        "def": 8,
        "hp": 25,
        "mana": 10,
        "crit_res": 0.02,
        "price": 60,
    },
    {
        "name": "Studded Leather",
        "rank": "Uncommon",
        "def": 11,
        "hp": 35,
        "mana": 5,
        "crit_res": 0.02,
        "price": 80,
    },
    # Rare
    {
        "name": "Chainmail Suit",
        "rank": "Rare",
        "def": 18,
        "hp": 60,
        "mana": 15,
        "crit_res": 0.04,
        "price": 180,
    },
    {
        "name": "Iron Plate Armor",
        "rank": "Rare",
        "def": 22,
        "hp": 80,
        "mana": 0,
        "crit_res": 0.05,
        "price": 220,
    },
    # Super Rare
    {
        "name": "Steel Cuirass",
        "rank": "Super Rare",
        "def": 35,
        "hp": 120,
        "mana": 20,
        "crit_res": 0.07,
        "price": 450,
    },
    {
        "name": "Mage Robe of Insight",
        "rank": "Super Rare",
        "def": 25,
        "hp": 100,
        "mana": 80,
        "crit_res": 0.06,
        "price": 480,
    },
    # Epic
    {
        "name": "Dragon Scale Mail",
        "rank": "Epic",
        "def": 55,
        "hp": 200,
        "mana": 40,
        "crit_res": 0.10,
        "price": 1000,
    },
    {
        "name": "Shadow Assassin Cloak",
        "rank": "Epic",
        "def": 48,
        "hp": 180,
        "mana": 60,
        "crit_res": 0.12,
        "price": 1100,
    },
    # Mythical
    {
        "name": "Celestial Aegis",
        "rank": "Mythical",
        "def": 85,
        "hp": 350,
        "mana": 120,
        "crit_res": 0.15,
        "price": 2500,
    },
    # Legendary
    {
        "name": "Armor of the Gods",
        "rank": "Legendary",
        "def": 130,
        "hp": 600,
        "mana": 200,
        "crit_res": 0.22,
        "price": 6000,
    },
]

POTIONS_POOL = [
    # Health Potions
    {
        "name": "Small Health Potion",
        "type": "hp",
        "val": 50,
        "price": 15,
        "cat": "Health",
    },
    {
        "name": "Medium Health Potion",
        "type": "hp",
        "val": 100,
        "price": 35,
        "cat": "Health",
    },
    {
        "name": "Large Health Potion",
        "type": "hp",
        "val": 250,
        "price": 80,
        "cat": "Health",
    },
    {
        "name": "Giant Health Potion",
        "type": "hp",
        "val": 500,
        "price": 180,
        "cat": "Health",
    },
    {
        "name": "Ultimate Health Potion",
        "type": "hp",
        "val": 99999,
        "price": 400,
        "cat": "Health",
    },
    # Mana Potions
    {
        "name": "Small Mana Potion",
        "type": "mana",
        "val": 30,
        "price": 15,
        "cat": "Mana",
    },
    {
        "name": "Medium Mana Potion",
        "type": "mana",
        "val": 75,
        "price": 35,
        "cat": "Mana",
    },
    {
        "name": "Large Mana Potion",
        "type": "mana",
        "val": 150,
        "price": 80,
        "cat": "Mana",
    },
    {
        "name": "Giant Mana Potion",
        "type": "mana",
        "val": 300,
        "price": 180,
        "cat": "Mana",
    },
    {
        "name": "Ultimate Mana Potion",
        "type": "mana",
        "val": 99999,
        "price": 400,
        "cat": "Mana",
    },
    # Mixed Potions
    {
        "name": "Minor Rejuvenation Potion",
        "type": "mixed",
        "val": 60,
        "price": 50,
        "cat": "Mixed",
    },
    {
        "name": "Major Rejuvenation Potion",
        "type": "mixed",
        "val": 200,
        "price": 150,
        "cat": "Mixed",
    },
    {
        "name": "Elixir of Life",
        "type": "mixed",
        "val": 99999,
        "price": 600,
        "cat": "Mixed",
    },
    # Buff Potions
    {
        "name": "Attack Potion",
        "type": "buff_atk",
        "val": 15,
        "price": 100,
        "cat": "Buff",
    },
    {
        "name": "Defense Potion",
        "type": "buff_def",
        "val": 15,
        "price": 100,
        "cat": "Buff",
    },
]

ENEMY_NAMES = {
    1: ["Goblin", "Wolf", "Slime", "Zombie", "Skeleton"],
    2: ["Orc", "Bandit", "Troll", "Dark Archer", "Giant Spider"],
    3: ["Vampire", "Werewolf", "Necromancer", "Ice Golem", "Fire Demon"],
    4: ["Sand Scorpion", "Desert Bandit", "Mummy", "Anubis Guard"],
    5: ["Corrupted Knight", "Gargoyle", "Lich", "Ghost Warrior"],
    6: ["Castle Guard", "Royal Archer", "Iron Golem", "Dark Priest"],
    7: ["Magma Fiend", "Fire Drake", "Lava Hound", "Hellhound"],
    8: ["Frost Wraith", "Ice Drake", "Snow Elemental", "Yeti"],
    9: ["Sun Warrior", "Sky Guardian", "Storm Griffin", "Archangel"],
    10: ["Demon Hound", "Infernal Fiend", "Void Crawler", "Shadow Fiend"],
}

BOSSES = {
    10: "Goblin King",
    20: "Forest Guardian",
    30: "Ancient Golem",
    40: "Vampire Lord",
    50: "Dragon Rider",
    60: "Demon General",
    70: "Ice Titan",
    80: "Shadow Emperor",
    90: "Celestial Dragon",
    100: "Ancient Demon King",
}

REGIONS = [
    "Village",
    "Forest",
    "Cave",
    "Desert",
    "Ruins",
    "Castle",
    "Volcano",
    "Frozen Mountain",
    "Sky Temple",
    "Demon Realm",
]

# =====================================================================
# GAME STATE OBJECT
# =====================================================================

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

# =====================================================================
# UTILITY FUNCTIONS
# =====================================================================


def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title.center(46)} ")
    print("=" * 50)


def get_input(prompt, valid_options):
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("Invalid choice! Please select a valid option.")


# =====================================================================
# SYSTEM IMPLEMENTATIONS
# =====================================================================


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

    # Starter Gear
    player["weapon"] = WEAPONS_POOL[0]  # Wooden Sword
    player["armor"] = ARMOR_POOL[0]  # Cloth Tunic
    player["inventory"].append(POTIONS_POOL[0].copy())  # Small HP
    player["inventory"].append(POTIONS_POOL[5].copy())  # Small Mana

    print(
        f"\nWelcome, {name} the {selected_class}! Your journey begins in Eldoria."
    )


def view_stats():
    print_header("PLAYER STATS")
    w_dmg = player["weapon"]["dmg"] if player["weapon"] else 0
    a_def = player["armor"]["def"] if player["armor"] else 0
    a_hp = player["armor"]["hp"] if player["armor"] else 0
    a_mana = player["armor"]["mana"] if player["armor"] else 0

    print(f"Name: {player['name']} | Class: {player['class']}")
    print(f"Level: {player['level']} | EXP: {player['exp']}/{player['max_exp']}")
    print(
        f"HP: {player['hp']}/{player['max_hp'] + a_hp} | Mana: {player['mana']}/{player['max_mana'] + a_mana}"
    )
    print(f"Attack: {player['atk']} (+{w_dmg}) | Defense: {player['def']} (+{a_def})")
    print(f"Critical Chance: {int((player['crit'] + (player['weapon']['crit_bonus'] if player['weapon'] else 0))*100)}%")
    print(f"Gold: {player['gold']}")
    print(
        f"Weapon: {player['weapon']['name'] if player['weapon'] else 'None'}"
    )
    print(f"Armor: {player['armor']['name'] if player['armor'] else 'None'}")
    print(f"Bosses Defeated: {player['bosses_defeated']}/10")


def level_up_check():
    while player["exp"] >= player["max_exp"] and player["level"] < 100:
        # Block leveling beyond regional cap if boss not defeated
        current_cap = (player["bosses_defeated"] + 1) * 10
        if player["level"] >= current_cap:
            print(
                f"\n[Cap Reached] Defeat the Level {current_cap} Boss to continue leveling!"
            )
            player["exp"] = player["max_exp"] - 1
            break

        player["exp"] -= player["max_exp"]
        player["level"] += 1
        player["max_exp"] = int(player["max_exp"] * 1.25)

        # Stat Gains
        player["max_hp"] += 20
        player["max_mana"] += 10
        player["atk"] += 4
        player["def"] += 2
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]

        print(
            f"\nLEVEL UP! You reached Level {player['level']}! All stats increased and resources fully restored!"
        )


def manage_inventory():
    while True:
        print_header("INVENTORY MANAGEMENT")
        print("1. View / Equip / Use Items")
        print("2. Unequip Weapon")
        print("3. Unequip Armor")
        print("4. Back")

        choice = get_input("Choose option: ", ["1", "2", "3", "4"])
        if choice == "1":
            if not player["inventory"]:
                print("Your inventory is empty!")
                continue
            print("\nInventory Contents:")
            for idx, item in enumerate(player["inventory"], 1):
                item_type = item.get("rank", item.get("cat", "Item"))
                print(f"{idx}. {item['name']} [{item_type}]")
            print(f"{len(player['inventory'])+1}. Back")

            sub_choice = input("Select item to inspect/use: ").strip()
            if sub_choice.isdigit():
                idx = int(sub_choice) - 1
                if 0 <= idx < len(player["inventory"]):
                    item = player["inventory"][idx]
                    print(f"\nSelected: {item['name']}")
                    print("1. Use/Equip | 2. Drop | 3. Cancel")
                    act = get_input("Select: ", ["1", "2", "3"])
                    if act == "1":
                        if "dmg" in item:  # Weapon
                            if item["req_lvl"] <= player["level"]:
                                if player["weapon"]:
                                    player["inventory"].append(
                                        player["weapon"]
                                    )
                                player["weapon"] = item
                                player["inventory"].pop(idx)
                                print(f"Equipped weapon: {item['name']}")
                            else:
                                print(
                                    f"Level too low! Requires Level {item['req_lvl']}."
                                )
                        elif "crit_res" in item:  # Armor
                            if player["armor"]:
                                player["inventory"].append(player["armor"])
                            player["armor"] = item
                            player["inventory"].pop(idx)
                            print(f"Equipped armor: {item['name']}")
                        elif "type" in item:  # Potion
                            use_potion(item)
                            player["inventory"].pop(idx)
                    elif act == "2":
                        player["inventory"].pop(idx)
                        print("Item discarded.")
        elif choice == "2":
            if player["weapon"]:
                player["inventory"].append(player["weapon"])
                print(f"Unequipped {player['weapon']['name']}")
                player["weapon"] = None
            else:
                print("No weapon equipped!")
        elif choice == "3":
            if player["armor"]:
                player["inventory"].append(player["armor"])
                print(f"Unequipped {player['armor']['name']}")
                player["armor"] = None
            else:
                print("No armor equipped!")
        else:
            break


def use_potion(potion):
    if potion["type"] == "hp":
        player["hp"] = min(
            player["max_hp"] + (player["armor"]["hp"] if player["armor"] else 0),
            player["hp"] + potion["val"],
        )
        print(f"Restored HP! Current HP: {player['hp']}")
    elif potion["type"] == "mana":
        player["mana"] = min(
            player["max_mana"]
            + (player["armor"]["mana"] if player["armor"] else 0),
            player["mana"] + potion["val"],
        )
        print(f"Restored Mana! Current Mana: {player['mana']}")
    elif potion["type"] == "mixed":
        player["hp"] = min(
            player["max_hp"] + (player["armor"]["hp"] if player["armor"] else 0),
            player["hp"] + potion["val"],
        )
        player["mana"] = min(
            player["max_mana"]
            + (player["armor"]["mana"] if player["armor"] else 0),
            player["mana"] + potion["val"],
        )
        print("Restored both HP and Mana!")


def shop():
    while True:
        print_header("VILLAGE SHOP")
        print("1. Buy Weapons")
        print("2. Buy Armor")
        print("3. Buy Potions")
        print("4. Sell Items")
        print("5. Exit Shop")

        choice = get_input("Choose option: ", ["1", "2", "3", "4", "5"])
        if choice in ["1", "2", "3"]:
            items = (
                WEAPONS_POOL
                if choice == "1"
                else (ARMOR_POOL if choice == "2" else POTIONS_POOL)
            )
            print("\nAvailable Items:")
            for idx, item in enumerate(items, 1):
                print(f"{idx}. {item['name']} - Price: {item['price']} Gold")
            print(f"{len(items)+1}. Cancel")

            sub_choice = input("Select item to buy: ").strip()
            if sub_choice.isdigit():
                idx = int(sub_choice) - 1
                if 0 <= idx < len(items):
                    item = items[idx]
                    if player["gold"] >= item["price"]:
                        player["gold"] -= item["price"]
                        player["inventory"].append(item.copy())
                        if "rank" in item and item["rank"] in [
                            "Super Rare",
                            "Epic",
                            "Mythical",
                            "Legendary",
                        ]:
                            player["rare_items_found"] += 1
                        if "dmg" in item:
                            player["weapons_collected"] += 1
                        print(f"Purchased {item['name']}!")
                    else:
                        print("Not enough Gold!")
        elif choice == "4":
            if not player["inventory"]:
                print("Nothing to sell!")
                continue
            print("\nYour Inventory (Sells for 50% value):")
            for idx, item in enumerate(player["inventory"], 1):
                val = item.get("price", 20) // 2
                print(f"{idx}. {item['name']} - Sell Price: {val} Gold")
            print(f"{len(player['inventory'])+1}. Cancel")

            sub_choice = input("Select item to sell: ").strip()
            if sub_choice.isdigit():
                idx = int(sub_choice) - 1
                if 0 <= idx < len(player["inventory"]):
                    item = player["inventory"].pop(idx)
                    val = item.get("price", 20) // 2
                    player["gold"] += val
                    print(f"Sold {item['name']} for {val} Gold!")
        else:
            break


# =====================================================================
# COMBAT SYSTEM
# =====================================================================


def generate_loot():
    roll = random.random() * 100
    if roll <= 0.1:
        rank = "Legendary"
    elif roll <= 1.0:
        rank = "Mythical"
    elif roll <= 4.0:
        rank = "Epic"
    elif roll <= 10.0:
        rank = "Super Rare"
    elif roll <= 25.0:
        rank = "Rare"
    elif roll <= 50.0:
        rank = "Uncommon"
    else:
        rank = "Common"

    pool = random.choice([WEAPONS_POOL, ARMOR_POOL])
    filtered = [i for i in pool if i.get("rank") == rank]
    if filtered:
        item = random.choice(filtered).copy()
        player["inventory"].append(item)
        print(f"\n[LOOT DROP] You found a {rank} item: {item['name']}!")
        if rank in ["Super Rare", "Epic", "Mythical", "Legendary"]:
            player["rare_items_found"] += 1
        if "dmg" in item:
            player["weapons_collected"] += 1


def battle(enemy_name, enemy_hp, enemy_atk, enemy_def, is_boss=False):
    print_header(f"BATTLE: {enemy_name}")
    curr_enemy_hp = enemy_hp
    defending = False
    turn = 0

    while curr_enemy_hp > 0 and player["hp"] > 0:
        turn += 1
        print(
            f"\n--- Turn {turn} --- | Player HP: {player['hp']} | Mana: {player['mana']}"
        )
        print(f"{enemy_name} HP: {curr_enemy_hp}/{enemy_hp}")
        print(
            "1. Attack  2. Skills  3. Heal  4. Use Potion  5. Defend  6. Inventory  7. View Stats  8. Run"
        )

        choice = get_input(
            "Action: ", ["1", "2", "3", "4", "5", "6", "7", "8"]
        )

        if choice == "1":  # Basic Attack
            w_dmg = player["weapon"]["dmg"] if player["weapon"] else 0
            w_crit = player["weapon"]["crit_bonus"] if player["weapon"] else 0
            total_atk = player["atk"] + w_dmg

            is_crit = random.random() < (player["crit"] + w_crit)
            dmg = max(1, total_atk - enemy_def)
            if is_crit:
                dmg = int(dmg * 1.5)
                print("CRITICAL HIT!")

            curr_enemy_hp -= dmg
            print(f"You dealt {dmg} damage to {enemy_name}!")

        elif choice == "2":  # Class Skills
            skills = CLASSES[player["class"]]["skills"]
            print("\nSelect Skill:")
            s_list = list(skills.keys())
            for idx, s in enumerate(s_list, 1):
                print(
                    f"{idx}. {s} (Cost: {skills[s]['cost']} Mana, Multiplier: {skills[s]['multiplier']}x)"
                )
            print(f"{len(s_list)+1}. Cancel")

            s_choice = input("Select: ").strip()
            if s_choice.isdigit() and 1 <= int(s_choice) <= len(s_list):
                s_name = s_list[int(s_choice) - 1]
                s_data = skills[s_name]
                if player["mana"] >= s_data["cost"]:
                    player["mana"] -= s_data["cost"]
                    w_dmg = player["weapon"]["dmg"] if player["weapon"] else 0
                    dmg = max(
                        1,
                        int((player["atk"] + w_dmg) * s_data["multiplier"])
                        - enemy_def,
                    )
                    curr_enemy_hp -= dmg
                    print(
                        f"You cast {s_name} dealing {dmg} damage to {enemy_name}!"
                    )
                else:
                    print("Not enough Mana!")
                    continue
            else:
                continue

        elif choice == "3":  # Rest/Heal
            m_cost = 15
            if player["mana"] >= m_cost:
                player["mana"] -= m_cost
                heal = 40
                player["hp"] = min(player["max_hp"], player["hp"] + heal)
                print(f"Used Heal magic! Restored {heal} HP.")
            else:
                print("Not enough Mana for Heal magic!")
                continue

        elif choice == "4":  # Use Potion
            pots = [i for i in player["inventory"] if "type" in i]
            if not pots:
                print("No potions in inventory!")
                continue
            for idx, p in enumerate(pots, 1):
                print(f"{idx}. {p['name']}")
            p_choice = input("Select potion: ").strip()
            if p_choice.isdigit() and 1 <= int(p_choice) <= len(pots):
                p_item = pots[int(p_choice) - 1]
                use_potion(p_item)
                player["inventory"].remove(p_item)
            else:
                continue

        elif choice == "5":  # Defend
            defending = True
            print("You brace for incoming attacks (50% damage reduction next turn).")

        elif choice == "6":  # Inventory
            manage_inventory()
            continue

        elif choice == "7":  # View Stats
            view_stats()
            continue

        elif choice == "8":  # Run
            if is_boss:
                print("You cannot run from a Boss battle!")
                continue
            if random.random() < 0.5:
                print("You successfully fled the battle!")
                return False
            else:
                print("Escape failed!")

        # Enemy Turn
        if curr_enemy_hp > 0:
            a_def = player["armor"]["def"] if player["armor"] else 0
            base_dmg = max(1, enemy_atk - (player["def"] + a_def))

            if is_boss and turn % 3 == 0:
                print(f"\n[SPECIAL ATTACK] {enemy_name} unleashes a power strike!")
                base_dmg = int(base_dmg * 1.5)

            if defending:
                base_dmg = int(base_dmg * 0.5)
                defending = False

            player["hp"] -= base_dmg
            print(f"{enemy_name} attacked you for {base_dmg} damage!")

            if player["hp"] <= 0:
                print("\nYou have been defeated in battle!")
                return False

    # Battle Won
    if curr_enemy_hp <= 0:
        print(f"\nVictory! You defeated {enemy_name}!")
        player["enemies_defeated"] += 1
        exp_gain = enemy_hp * 2
        gold_gain = enemy_atk * 3
        player["exp"] += exp_gain
        player["gold"] += gold_gain
        print(f"Gained {exp_gain} EXP and {gold_gain} Gold!")

        if is_boss:
            player["bosses_defeated"] += 1

        generate_loot()
        level_up_check()
        return True


# =====================================================================
# FILE HANDLING (SAVE / LOAD)
# =====================================================================


def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player, f)
    print("Game state saved successfully!")


def load_game():
    global player
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            player = json.load(f)
        print("Game loaded successfully!")
        return True
    else:
        print("No save file found!")
        return False


# =====================================================================
# GAME FLOW & MENUS
# =====================================================================


def game_over():
    print_header("GAME OVER")
    print("1. Retry (Load Last Save)")
    print("2. Main Menu")
    print("3. Exit Game")
    choice = get_input("Choose option: ", ["1", "2", "3"])
    if choice == "1":
        if load_game():
            game_loop()
    elif choice == "2":
        main_menu()
    else:
        sys.exit()


def victory_screen():
    elapsed_time = int(time.time() - player["start_time"])
    mins, secs = divmod(elapsed_time, 60)
    score = (
        (player["level"] * 100)
        + player["gold"]
        + (player["bosses_defeated"] * 500)
    )

    print_header("VICTORY - Eldoria Restored!")
    print("Congratulations! You defeated the Ancient Demon King!")
    print(f"Player Name: {player['name']}")
    print(f"Final Level: {player['level']}")
    print(f"Total Gold: {player['gold']}")
    print(f"Bosses Defeated: {player['bosses_defeated']}")
    print(f"Enemies Defeated: {player['enemies_defeated']}")
    print(f"Weapons Collected: {player['weapons_collected']}")
    print(f"Rare Items Found: {player['rare_items_found']}")
    print(f"Total Play Time: {mins}m {secs}s")
    print(f"Final Score: {score}")
    sys.exit()


def game_loop():
    while True:
        region_idx = min(player["bosses_defeated"], 9)
        current_region = REGIONS[region_idx]

        print_header(f"WORLD MAP - Region: {current_region}")
        print("1. Explore / Battle Monsters")
        print(f"2. Challenge Region Boss (Level {(region_idx+1)*10})")
        print("3. Visit Village Shop")
        print("4. Inventory Management")
        print("5. View Character Stats")
        print("6. Save Game")
        print("7. Return to Main Menu")

        choice = get_input("Select action: ", ["1", "2", "3", "4", "5", "6", "7"])

        if choice == "1":
            tier = min(10, (player["level"] // 10) + 1)
            e_name = random.choice(ENEMY_NAMES[tier])
            e_hp = 30 + (player["level"] * 12)
            e_atk = 8 + (player["level"] * 3)
            e_def = 2 + (player["level"] * 1)

            success = battle(e_name, e_hp, e_atk, e_def)
            if not success and player["hp"] <= 0:
                game_over()

        elif choice == "2":
            boss_lvl = (player["bosses_defeated"] + 1) * 10
            boss_name = BOSSES[boss_lvl]

            print(f"\nChallenging Region Boss: {boss_name}!")
            b_hp = 150 + (boss_lvl * 25)
            b_atk = 15 + (boss_lvl * 5)
            b_def = 5 + (boss_lvl * 2)

            success = battle(boss_name, b_hp, b_atk, b_def, is_boss=True)
            if success:
                if player["bosses_defeated"] >= 10:
                    victory_screen()
            elif player["hp"] <= 0:
                game_over()

        elif choice == "3":
            shop()
        elif choice == "4":
            manage_inventory()
        elif choice == "5":
            view_stats()
        elif choice == "6":
            save_game()
        elif choice == "7":
            break


def display_instructions():
    print_header("INSTRUCTIONS")
    print(
        "- Defeat enemies to gain EXP, Gold, and Loot across 10 regions of Eldoria."
    )
    print(
        "- Every 10 levels, you face a mandatory Boss required to unlock the next region."
    )
    print("- Equip stronger weapons and armor to increase Attack and Defense.")
    print("- Utilize skills and potions strategically in turn-based combat.")
    print("- Defeat the Ancient Demon King at Level 100 to save Eldoria!")


def main_menu():
    while True:
        print_header("LEGENDS OF THE FORGOTTEN REALM")
        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        choice = get_input("Choose option: ", ["1", "2", "3", "4"])
        if choice == "1":
            create_character()
            game_loop()
        elif choice == "2":
            if load_game():
                game_loop()
        elif choice == "3":
            display_instructions()
        elif choice == "4":
            print("Thank you for playing!")
            sys.exit()


if __name__ == "__main__":
    main_menu()