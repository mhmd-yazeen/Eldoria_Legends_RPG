# combat.py
import random
from config import CLASSES, WEAPONS_POOL, ARMOR_POOL
from player import player, level_up_check, view_stats
from inventory import use_potion, manage_inventory
from utils import print_header, get_input


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
        print(f"\n--- Turn {turn} --- | Player HP: {player['hp']} | Mana: {player['mana']}")
        print(f"{enemy_name} HP: {curr_enemy_hp}/{enemy_hp}")
        print("1. Attack  2. Skills  3. Heal  4. Use Potion  5. Defend  6. Inventory  7. View Stats  8. Run")

        choice = get_input("Action: ", ["1", "2", "3", "4", "5", "6", "7", "8"])

        if choice == "1":
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

        elif choice == "2":
            skills = CLASSES[player["class"]]["skills"]
            print("\nSelect Skill:")
            s_list = list(skills.keys())
            for idx, s in enumerate(s_list, 1):
                print(f"{idx}. {s} (Cost: {skills[s]['cost']} Mana, Multiplier: {skills[s]['multiplier']}x)")
            print(f"{len(s_list)+1}. Cancel")

            s_choice = input("Select: ").strip()
            if s_choice.isdigit() and 1 <= int(s_choice) <= len(s_list):
                s_name = s_list[int(s_choice) - 1]
                s_data = skills[s_name]
                if player["mana"] >= s_data["cost"]:
                    player["mana"] -= s_data["cost"]
                    w_dmg = player["weapon"]["dmg"] if player["weapon"] else 0
                    dmg = max(1, int((player["atk"] + w_dmg) * s_data["multiplier"]) - enemy_def)
                    curr_enemy_hp -= dmg
                    print(f"You cast {s_name} dealing {dmg} damage to {enemy_name}!")
                else:
                    print("Not enough Mana!")
                    continue
            else:
                continue

        elif choice == "3":
            m_cost = 15
            if player["mana"] >= m_cost:
                player["mana"] -= m_cost
                heal = 40
                player["hp"] = min(player["max_hp"], player["hp"] + heal)
                print(f"Used Heal magic! Restored {heal} HP.")
            else:
                print("Not enough Mana for Heal magic!")
                continue

        elif choice == "4":
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

        elif choice == "5":
            defending = True
            print("You brace for incoming attacks (50% damage reduction next turn).")

        elif choice == "6":
            manage_inventory()
            continue

        elif choice == "7":
            view_stats()
            continue

        elif choice == "8":
            if is_boss:
                print("You cannot run from a Boss battle!")
                continue
            if random.random() < 0.5:
                print("You successfully fled the battle!")
                return False
            else:
                print("Escape failed!")

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