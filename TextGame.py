def master():
    inventory = []

    rooms = {
        "Masked Smile Room": {
            "South": "Overthinking Hall",
            "West": "Endless Laundry room",
            "East": "Mirror Room",
            "North": "Burnt Food Kitchen"
            },
        "Overthinking Hall": {
            "East": "Restless Bedroom",
            "North": "Masked Smile Room",
            "item": "Clarity Lantern"
            },
        "Restless Bedroom": {
            "West": "Overthinking Hall",
            "item": "Sleep Feather"
            },
        "Endless Laundry room": {
            "South": "Later Closet",
            "East": "Masked Smile Room",
            "item": "Patience Thread"
            },
        "Later Closet": {
            "North": "Endless Laundry room",
            "item": "Action Key"
            },
        "Mirror Room": {
            "West": "Masked Smile Room",
            "North": "Mind Room",
            "item": "Self-Worth"
            },
        "Burnt Food Kitchen": {
            "South": "Masked Smile Room",
            "East": "Unfinished Projects room",
            "item": "Good Enough Recipe"
            },
        "Unfinished Projects room": {
            "West": "Burnt Food Kitchen",
            "item": "Completion Needle"
            },
        "Mind Room": {"South": "Mirror Room"
                      }
    }
    current_room = "Masked Smile Room"

    welcome_menu()


    while True:
        current_status(current_room, inventory, rooms)
        if current_room == "Mind Room":
            if len(inventory) == 7:
                print("You gathered everything you needed and defeated the Crushing Weight!")
                print("Congratulations! You win!")
            else:
                print("You entered too soon...")
                print("The Crushing Weight defeated you. Game Over!")
            break

        move = input("Where do you want to go?\n").lower().strip()

        if move == "exit":
            print("Thanks for playing!")
            break

        move = move.split()

        if len(move) < 2:
            print("Invalid command.")
            continue

        command = move[0]
        option = " ".join(move[1:])
        option = option.title()

        if command == 'go':
            if option in rooms[current_room]:
                current_room = rooms[current_room][option]
            else:
                print("You can't go that way!")

        elif command == "get":
            if "item" in rooms[current_room] and rooms[current_room]["item"] == option:
                inventory.append(option)
                del rooms[current_room]["item"]
                print(option, "collected!")
            else:
                print("That item is not in this room.")

        else:
            print("Invalid Command")


def welcome_menu():
        print("=" * 50)
        print("       Hidden Struggles of a Mother")
        print("=" * 50)
        print("Collect all 7 items before facing the Crushing Weight!")
        print()
        print("Commands:")
        print("  Move: go North, go South, go East, or go West")
        print("  Collect an item: get <item name>")
        print("  Quit the game: exit")
        print("=" * 50)
        print()


def current_status(current_room, inventory, rooms):
    print("=" * 50)
    print("                      STATUS")
    print("=" * 50)
    print("You are in:", current_room)
    if len(inventory) == 0:
        print("Inventory: Empty")
    else:
        print("Inventory:", ", ".join(inventory))
    print("Connected Rooms:")
    for direction in rooms[current_room]:
        if direction != "item":
            print("-", direction, "->", rooms[current_room][direction])

    if "item" in rooms[current_room]:
        print("Item in room:", rooms[current_room]["item"])
    print("=" * 50)

master()

