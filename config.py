# config.py

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
    # Common
    {"name": "Wooden Sword", "rank": "Common", "dmg": 5, "crit_bonus": 0.00, "price": 20, "req_lvl": 1},
    {"name": "Rusty Axe", "rank": "Common", "dmg": 6, "crit_bonus": 0.00, "price": 25, "req_lvl": 1},
    {"name": "Training Bow", "rank": "Common", "dmg": 4, "crit_bonus": 0.00, "price": 18, "req_lvl": 1},
    # Uncommon
    {"name": "Bronze Dagger", "rank": "Uncommon", "dmg": 10, "crit_bonus": 0.02, "price": 50, "req_lvl": 5},
    {"name": "Apprentice Staff", "rank": "Uncommon", "dmg": 12, "crit_bonus": 0.02, "price": 60, "req_lvl": 5},
    {"name": "Hunting Bow", "rank": "Uncommon", "dmg": 11, "crit_bonus": 0.02, "price": 55, "req_lvl": 5},
    # Rare
    {"name": "Iron Sword", "rank": "Rare", "dmg": 20, "crit_bonus": 0.05, "price": 120, "req_lvl": 10},
    {"name": "Steel Axe", "rank": "Rare", "dmg": 24, "crit_bonus": 0.05, "price": 150, "req_lvl": 12},
    {"name": "Long Bow", "rank": "Rare", "dmg": 22, "crit_bonus": 0.05, "price": 135, "req_lvl": 11},
    # Super Rare
    {"name": "Crystal Blade", "rank": "Super Rare", "dmg": 38, "crit_bonus": 0.08, "price": 300, "req_lvl": 20},
    {"name": "Shadow Dagger", "rank": "Super Rare", "dmg": 35, "crit_bonus": 0.08, "price": 280, "req_lvl": 20},
    {"name": "Lightning Bow", "rank": "Super Rare", "dmg": 40, "crit_bonus": 0.08, "price": 320, "req_lvl": 22},
    # Epic
    {"name": "Flame Sword", "rank": "Epic", "dmg": 65, "crit_bonus": 0.12, "price": 700, "req_lvl": 35},
    {"name": "Ice Spear", "rank": "Epic", "dmg": 68, "crit_bonus": 0.12, "price": 750, "req_lvl": 38},
    {"name": "Thunder Hammer", "rank": "Epic", "dmg": 72, "crit_bonus": 0.12, "price": 800, "req_lvl": 40},
    # Mythical
    {"name": "Phoenix Blade", "rank": "Mythical", "dmg": 110, "crit_bonus": 0.18, "price": 1500, "req_lvl": 55},
    {"name": "Demon Slayer", "rank": "Mythical", "dmg": 120, "crit_bonus": 0.18, "price": 1800, "req_lvl": 60},
    {"name": "Celestial Staff", "rank": "Mythical", "dmg": 115, "crit_bonus": 0.18, "price": 1650, "req_lvl": 58},
    # Legendary
    {"name": "Dragon King's Sword", "rank": "Legendary", "dmg": 200, "crit_bonus": 0.25, "price": 4000, "req_lvl": 80},
    {"name": "Blade of Eternity", "rank": "Legendary", "dmg": 220, "crit_bonus": 0.25, "price": 5000, "req_lvl": 85},
    {"name": "Bow of the Gods", "rank": "Legendary", "dmg": 210, "crit_bonus": 0.25, "price": 4500, "req_lvl": 82},
]

ARMOR_POOL = [
    {"name": "Cloth Tunic", "rank": "Common", "def": 3, "hp": 10, "mana": 5, "crit_res": 0.01, "price": 20},
    {"name": "Leather Vest", "rank": "Common", "def": 5, "hp": 15, "mana": 0, "crit_res": 0.01, "price": 30},
    {"name": "Padded Armor", "rank": "Uncommon", "def": 8, "hp": 25, "mana": 10, "crit_res": 0.02, "price": 60},
    {"name": "Studded Leather", "rank": "Uncommon", "def": 11, "hp": 35, "mana": 5, "crit_res": 0.02, "price": 80},
    {"name": "Chainmail Suit", "rank": "Rare", "def": 18, "hp": 60, "mana": 15, "crit_res": 0.04, "price": 180},
    {"name": "Iron Plate Armor", "rank": "Rare", "def": 22, "hp": 80, "mana": 0, "crit_res": 0.05, "price": 220},
    {"name": "Steel Cuirass", "rank": "Super Rare", "def": 35, "hp": 120, "mana": 20, "crit_res": 0.07, "price": 450},
    {"name": "Mage Robe of Insight", "rank": "Super Rare", "def": 25, "hp": 100, "mana": 80, "crit_res": 0.06, "price": 480},
    {"name": "Dragon Scale Mail", "rank": "Epic", "def": 55, "hp": 200, "mana": 40, "crit_res": 0.10, "price": 1000},
    {"name": "Shadow Assassin Cloak", "rank": "Epic", "def": 48, "hp": 180, "mana": 60, "crit_res": 0.12, "price": 1100},
    {"name": "Celestial Aegis", "rank": "Mythical", "def": 85, "hp": 350, "mana": 120, "crit_res": 0.15, "price": 2500},
    {"name": "Armor of the Gods", "rank": "Legendary", "def": 130, "hp": 600, "mana": 200, "crit_res": 0.22, "price": 6000},
]

POTIONS_POOL = [
    {"name": "Small Health Potion", "type": "hp", "val": 50, "price": 15, "cat": "Health"},
    {"name": "Medium Health Potion", "type": "hp", "val": 100, "price": 35, "cat": "Health"},
    {"name": "Large Health Potion", "type": "hp", "val": 250, "price": 80, "cat": "Health"},
    {"name": "Giant Health Potion", "type": "hp", "val": 500, "price": 180, "cat": "Health"},
    {"name": "Ultimate Health Potion", "type": "hp", "val": 99999, "price": 400, "cat": "Health"},
    {"name": "Small Mana Potion", "type": "mana", "val": 30, "price": 15, "cat": "Mana"},
    {"name": "Medium Mana Potion", "type": "mana", "val": 75, "price": 35, "cat": "Mana"},
    {"name": "Large Mana Potion", "type": "mana", "val": 150, "price": 80, "cat": "Mana"},
    {"name": "Giant Mana Potion", "type": "mana", "val": 300, "price": 180, "cat": "Mana"},
    {"name": "Ultimate Mana Potion", "type": "mana", "val": 99999, "price": 400, "cat": "Mana"},
    {"name": "Minor Rejuvenation Potion", "type": "mixed", "val": 60, "price": 50, "cat": "Mixed"},
    {"name": "Major Rejuvenation Potion", "type": "mixed", "val": 200, "price": 150, "cat": "Mixed"},
    {"name": "Elixir of Life", "type": "mixed", "val": 99999, "price": 600, "cat": "Mixed"},
    {"name": "Attack Potion", "type": "buff_atk", "val": 15, "price": 100, "cat": "Buff"},
    {"name": "Defense Potion", "type": "buff_def", "val": 15, "price": 100, "cat": "Buff"},
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
    "Village", "Forest", "Cave", "Desert", "Ruins",
    "Castle", "Volcano", "Frozen Mountain", "Sky Temple", "Demon Realm",
]