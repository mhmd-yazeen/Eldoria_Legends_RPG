# Legends of the Forgotten Realm (Eldoria RPG)

A feature-complete, text-based RPG written in Python. Experience turn-based strategic combat, character progression, inventory management, shop transactions, and dynamic loot generation across 10 distinct regions of Eldoria.

---

## Features

- **Character Classes:** Choose between Warrior, Mage, Archer, and Assassin, each with distinct base stats and unique combat skills.
- **Turn-Based Combat:** Engage in tactical battles with options to attack, cast skills, heal, use potions, defend, or run.
- **Equipment & Items:** Collect and equip weapons and armor spanning multiple rarity ranks (Common to Legendary).
- **Dynamic Loot System:** Defeat enemies to earn experience, gold, and random item drops based on rarity percentages[cite: 1].
- **Region & Boss Progression:** Journey through 10 distinct regions with capped level thresholds until regional bosses are defeated[cite: 1].
- **Persistence:** Save and load your game progress locally using JSON serialization[cite: 1].

---

## Class Overview

| Class | Specialization | Key Stats |
| :--- | :--- | :--- |
| **Warrior**[cite: 1] | Tank / High Survivability[cite: 1] | High HP/Def, Low Mana[cite: 1] |
| **Mage**[cite: 1] | Burst Magic Damage[cite: 1] | High Mana/Atk, Low Def[cite: 1] |
| **Archer**[cite: 1] | Critical Damage[cite: 1] | Balanced Stats, High Crit[cite: 1] |
| **Assassin**[cite: 1] | Single-Target Burst[cite: 1] | High Atk/Crit, Low HP[cite: 1] |

---

## Requirements

- Python 3.6+[cite: 1]
- No external third-party dependencies required (uses built-in `json`, `os`, `random`, `sys`, and `time` modules)[cite: 1].

---

## Installation & Running

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/eldoria-rpg.git](https://github.com/your-username/eldoria-rpg.git)
   cd eldoria-rpg
mm
