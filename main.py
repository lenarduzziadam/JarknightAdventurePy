from look import Look, create_default_world


def exploration_loop(rooms, start_room):
    current_room = start_room
    Look(rooms[current_room]).describe()
    while True:
        command = input("What do you do next? (look/go <direction>/proceed/quit): ").strip()
        if not command:
            continue
        normalized = command.lower()
        if normalized == 'look':
            Look(rooms[current_room]).describe()
            continue
        if normalized.startswith('go '):
            _, direction = normalized.split(' ', 1)
            next_room = rooms[current_room].exits.get(direction)
            if next_room:
                current_room = next_room
                print(f"You head {direction}.")
                Look(rooms[current_room]).describe()
            else:
                print("You can't go that way from here.")
            continue
        if normalized == 'proceed':
            return current_room
        if normalized == 'quit':
            print("Leaving the adventure for now.")
            return None
        print("Try 'look', 'go <direction>', 'proceed', or 'quit'.")


def main():
    rooms = create_default_world()
    while True:
        try:
            user_input = input("Do you wish to join Jarknight on his adventure? (yes/no): ")
            if user_input.lower() == 'no':
                print("Exiting the program.")
                break
            if user_input.lower() != 'yes':
                print("Please answer with 'yes' or 'no'.")
                continue
            print("Jarknight: 'Great! Let's begin our adventure!'")
            current_room = exploration_loop(rooms, 'village')
            if current_room is None:
                break
            number = float(input("Enter a number to divide 100 by: "))
            result = 100 / number
            print(f"100 divided by {number} is {result}")
            print("Thank you for joining Jarknight on his adventure oh no a Demon lord appeared!")

            user_input = input("Do you want to fight the Demon lord? (yes/no): ")
            if user_input.lower() == 'yes':
                print("Jarknight: 'For glory!'")
                print("You bravely fought the Demon lord and emerged victorious!")
            else:
                print("Jarknight: 'Retreating for now, but we'll be back!'")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()