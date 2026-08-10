# main.py
import random
import sys
import time

from config import ENEMY_NAMES, BOSSES, REGIONS
from utils import print_header, get_input
from player import player, create_character, view_stats
from inventory import shop, manage_inventory
from combat import battle
from storage import save_game, load_game


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
    print("- Defeat enemies to gain EXP, Gold, and Loot across 10 regions of Eldoria.")
    print("- Every 10 levels, you face a mandatory Boss required to unlock the next region.")
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