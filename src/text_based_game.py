# Student Name: Rahni Martin
# IT-140: Introduction to Scripting
# Project Two: Text-Based Adventure Game (Dragon Text Game)

def show_instructions():
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("To quit the game: exit")
    print("-" * 50)


def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item not in inventory:
            print(f"You see a {item}")
    print("-" * 50)


def main():
    rooms = {
        'Great Hall': {
            'South': 'Bedroom',
            'North': 'Dungeon',
            'East': 'Kitchen',
            'West': 'Library'
        },
        'Bedroom': {
            'North': 'Great Hall',
            'East': 'Cellar',
            'item': 'Armor'
        },
        'Cellar': {
            'West': 'Bedroom',
            'item': 'Helmet'
        },
        'Dungeon': {
            'South': 'Great Hall',
            'East': 'Armory',
            'item': 'Sword'
        },
        'Armory': {
            'West': 'Dungeon',
            'item': 'Shield'
        },
        'Kitchen': {
            'West': 'Great Hall',
            'East': 'Dining Room',
            'item': 'Potion'
        },
        'Library': {
            'East': 'Great Hall',
            'item': 'Key'
        },
        'Dining Room': {
            'West': 'Kitchen',
            'item': 'Dragon'
        }
    }

    current_room = 'Great Hall'
    inventory = []
    total_items_needed = 6

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        if "item" in rooms[current_room] and rooms[current_room]["item"] == 'Dragon':
            if len(inventory) == total_items_needed:
                print("\nCongratulations! You have collected all items and defeated the dragon!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("\nNOM NOM...GAME OVER!")
                print("You entered the Dragon's lair without all 6 items!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break

        user_input = input("Enter your move: ").strip().split()

        if not user_input:
            print("Invalid command! Please try again.")
            continue

        command = user_input[0].lower()

        if command == 'exit':
            print("Thanks for playing!")
            break

        elif command == 'go':
            if len(user_input) < 2:
                print("Go where? Please specify a direction (e.g., 'go North').")
                continue

            direction = user_input[1].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        elif command == 'get':
            if len(user_input) < 2:
                print("Get what? Please specify an item (e.g., 'get Armor').")
                continue

            target_item = " ".join(user_input[1:]).title()

            if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == target_item.lower():
                actual_item = rooms[current_room]["item"]
                if actual_item not in inventory:
                    inventory.append(actual_item)
                    print(f"You got the {actual_item}!")
                else:
                    print(f"You already have the {actual_item} in your inventory.")
            else:
                print(f"Can't get {target_item}!")

        else:
            print("Invalid command! Valid commands are 'go [direction]' or 'get [item]'.")


if __name__ == "__main__":
    main()
