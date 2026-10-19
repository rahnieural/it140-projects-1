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

    # Check if the current room contains an item and if the player hasn't picked it up yet
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item not in inventory:
            print(f"You see a {item}")
    print("-" * 50)


def main():
    # Dictionary linking rooms to directions and assigning one item per room
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
            'item': 'Dragon' # Villain room
        }
    }

    # Initialize starting game variables
    current_room = 'Great Hall'
    inventory = []
    total_items_needed = 6
    
    # Display initial instructions
    show_instructions()

    # Core gameplay loop
    while True:
        # Display current status at the start of each turn
        show_status(current_room, inventory, rooms)

        # Check for villain / end game condition upon entering room
        if "item" in rooms[current_room] and rooms[current_room]["item"] == 'Dragon':
            if len(inventory) == total_items_needed:
                print("\nCongratulations! You have collected all items and defeated the dragon!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("\nNOM NOM...GAME OVER!")
                print("You entered the Dragon's lair without all 6 items!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break # Exit game loop on win or loss

        # Prompt player for move input
        user_input = input("Enter your move: ").strip().split()

        # Input validation for empty input
        if not user_input:
            print("Invalid command! Please try again.")
            continue

        # Extract primary command word
        command = user_input[0].lower()

        # Handle exit command
        if command == 'exit':
            print("Thanks for playing!")
            break

        # Handle movement command ('go')
        elif command == 'go':
            if len(user_input) < 2:
                print("Go where? Please specify a direction (e.g., 'go North').")
                continue

            direction = user_input[1].capitalize()

            # Check if valid direction exists for current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Handle item collection command ('get')
        elif command == 'get':
            if len(user_input) < 2:
                print("Get what? Please specify an item (e.g., 'get Armor').")
                continue

            # Join remaining input tokens in case of multi-word items
            target_item = " ".join(user_input[1:]).title()

            # Validate item existence in current room
            if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == target_item.lower():
                actual_item = rooms[current_room]["item"]
                if actual_item not in inventory:
                    inventory.append(actual_item)
                    print(f"You got the {actual_item}!")
                else:
                    print(f"You already have the {actual_item} in your inventory.")
            else:
                print(f"Can't get {target_item}!")

        # Handle invalid action command
        else:
            print("Invalid command! Valid commands are 'go [direction]' or 'get [item]'.")

# Run main function when executed
if __name__ == "__main__":
    main()
