# Open the input file for reading
with open("input.txt", "r") as file:
    # Initialize a counter for successful conditions
    successful_conditions_counter = 0

    # Read each line from the file
    for line in file:
        # Extract the game number and bags information
        game_number, bags_info = line.split(':', 1)  # Split only once to separate game number and bags

        # Split the bags information into individual bags
        bags = bags_info.split(';')

        # Initialize a flag to track conditions for the current game
        conditions_met = True

        # Iterate through each bag in the current game
        for bag_index, bag in enumerate(bags, start=1):
            # Extract the colors and counts from the bag description
            bag_parts = bag.strip().split(', ')

            # Check if the bag description has the expected format
            for part in bag_parts:
                count, color = part.split()

                # Check conditions for each color in the current bag
                if color == "red" and int(count) > 12:
                    conditions_met = False
                    break
                elif color == "green" and int(count) > 13:
                    conditions_met = False
                    break
                elif color == "blue" and int(count) > 14:
                    conditions_met = False
                    break

        # If all conditions are true for the current game, increment the counter
        if conditions_met:
            # Extract the numeric part from the game number and add to the counter
            game_number_numeric = int(''.join(filter(str.isdigit, game_number)))
            successful_conditions_counter += game_number_numeric
            print(f"All conditions met in {game_number.strip()}")

# Print the total count of successful conditions
print(f"Total number of successful conditions: {successful_conditions_counter}")
