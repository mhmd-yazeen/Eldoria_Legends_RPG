# inventory.py
from player import player
from config import WEAPONS_POOL, ARMOR_POOL, POTIONS_POOL
from utils import print_header, get_input


def use_potion(potion):
    if potion["type"] == "hp":
        player["hp"] = min(
            player["max_hp"] + (player["armor"]["hp"] if player["armor"] else 0),
            player["hp"] + potion["val"],
        )
        print(f"Restored HP! Current HP: {player['hp']}")
    elif potion["type"] == "mana":
        player["mana"] = min(
            player["max_mana"] + (player["armor"]["mana"] if player["armor"] else 0),
            player["mana"] + potion["val"],
        )
        print(f"Restored Mana! Current Mana: {player['mana']}")
    elif potion["type"] == "mixed":
        player["hp"] = min(
            player["max_hp"] + (player["armor"]["hp"] if player["armor"] else 0),
            player["hp"] + potion["val"],
        )
        player["mana"] = min(
            player["max_mana"] + (player["armor"]["mana"] if player["armor"] else 0),
            player["mana"] + potion["val"],
        )
        print("Restored both HP and Mana!")


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
                        if "dmg" in item:
                            if item["req_lvl"] <= player["level"]:
                                if player["weapon"]:
                                    player["inventory"].append(player["weapon"])
                                player["weapon"] = item
                                player["inventory"].pop(idx)
                                print(f"Equipped weapon: {item['name']}")
                            else:
                                print(f"Level too low! Requires Level {item['req_lvl']}.")
                        elif "crit_res" in item:
                            if player["armor"]:
                                player["inventory"].append(player["armor"])
                            player["armor"] = item
                            player["inventory"].pop(idx)
                            print(f"Equipped armor: {item['name']}")
                        elif "type" in item:
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