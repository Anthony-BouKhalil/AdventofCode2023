# Initialize a variable to store the sum of powers
sum_of_powers = 0

# Open the input file for reading
with open("input.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Extract the game number and bags information
        game_number, bags_info = line.split(':', 1)  # Split only once to separate game number and bags

        # Split the bags information into individual bags
        bags = bags_info.split(';')

        # Initialize variables to track maximum counts for each color
        max_red = 0
        max_green = 0
        max_blue = 0

        # Iterate through each bag in the current game
        for bag in bags:
            # Extract the colors and counts from the bag description
            bag_parts = bag.strip().split(', ')

            # Check if the bag description has the expected format
            for part in bag_parts:
                count, color = part.split()

                # Update maximum counts for each color
                count = int(count)
                if color == "red":
                    max_red = max(max_red, count)
                elif color == "green":
                    max_green = max(max_green, count)
                elif color == "blue":
                    max_blue = max(max_blue, count)

        # Calculate the power for the current game
        power = max_red * max_green * max_blue

        # Add the power to the sum_of_powers variable
        sum_of_powers += power

        # Print the maximum set of cubes for the current game
        print(f"Maximum set of cubes for {game_number.strip()}: {max_red} red, {max_green} green, {max_blue} blue")

# Print the sum of powers for all games
print(f"Sum of powers: {sum_of_powers}")

