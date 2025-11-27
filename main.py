

while True:
    try:
        user_input = input("Do you wish to join Jarknight on his adventure? (yes/no): ")
        if user_input.lower() == 'no':
            print("Exiting the program.")
            break
        elif user_input.lower() != 'yes':
            print("Please answer with 'yes' or 'no'.")
            continue
        print(f"Jarkinight: 'Great! Let's begin our adventure!'")
        number = float(input("Enter a number to divide 100 by: "))
        result = 100 / number
        print(f"100 divided by {number} is {result}")
        print ("Thank you for joining Jarknight on his adventure oh no a Demon lord appeared!")

        user_input = input("Do you want to fight the Demon lord? (yes/no): ")
        if user_input.lower() == 'yes':
            print("Jarknight: 'For glory!'")
            # Simulate a fight sequence
            print("You bravely fought the Demon lord and emerged victorious!")
        else:
            print("Jarknight: 'Retreating for now, but we'll be back!'")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")