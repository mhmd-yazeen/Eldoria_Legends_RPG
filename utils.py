# utils.py

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