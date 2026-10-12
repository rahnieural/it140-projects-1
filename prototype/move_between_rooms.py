"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"}
}

# TODO: Set the player's starting room for the simplified prototype.
current_room = 'Great Hall'

# Display game instructions
print("Welcome to the Simplified Dragon Text Game!")
print("Commands: go south, go north, go east, go west, or exit.\n")

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
# 1. Display the current room.
# 2. Prompt for a movement command or "exit".
# 3. Branch for a valid move, exit, or invalid input.
# 4. Update the room only after a valid movement command.
# 5. Continue until the required exit condition is reached.
while current_room != 'exit':
    # 1. Display the current room
    print(f"You are in the {current_room}.")
    
    # 2. Prompt for a movement command or "exit"
    command = input("Enter your move: ").strip().lower()
    
    # 3. Branch for a valid move, exit, or invalid input
    if command == 'exit':
        current_room = 'exit'
        print("Thank you for playing. Goodbye!")
        break
        
    # Extract direction if user types "go [direction]" or just the direction name
    if command.startswith('go '):
        direction = command.split(' ', 1)[1]
    else:
        direction = command
        
    # 4. Update the room only after a valid movement command
    if direction in rooms.get(current_room, {}):
        current_room = rooms[current_room][direction]
    else:
        # Input validation / error message for invalid commands
        print("Invalid move! You can't go that way.\n")

# TODO: Run and debug all milestone cases in prototype/README.md.
