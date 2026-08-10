# storage.py
import json
import os
import player as player_module


def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player_module.player, f)
    print("Game state saved successfully!")


def load_game():
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            loaded_data = json.load(f)
            player_module.player.clear()
            player_module.player.update(loaded_data)
        print("Game loaded successfully!")
        return True
    else:
        print("No save file found!")
        return False