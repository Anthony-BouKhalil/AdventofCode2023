# Dictionary to store results
matching_counts = {}
card_points = {}
total_points = 0  # Total counter for the points of all cards

# Read input data from a file
with open('input.txt', 'r') as file:
    # Iterate over each line and extract relevant information
    for line in file:
        # Find the position of the '|' symbol
        separator_index = line.find('|')

        # Extract card number and numbers above and below the '|'
        card_number = int(line.split(':')[0].split()[-1])
        above_numbers = list(map(int, line[line.find(':')+1:separator_index].split()))
        below_numbers = list(map(int, line[separator_index + 1:].split()))
        print(above_numbers)
        print(below_numbers)

        # Count how many times numbers in above_numbers appear in below_numbers
        count = len(set(above_numbers) & set(below_numbers))

        # Calculate points based on the rules
        points = 2 ** (count - 1) if count > 0 else 0

        # Update the total counter
        total_points += points

        # Append the count and points to the dictionaries
        matching_counts[card_number] = count
        card_points[card_number] = points

# Print the matching counts, points, and total points
for card_number, count in matching_counts.items():
    points = card_points[card_number]
    print(f"Card {card_number}: Matching count: {count}, Points: {points}")

# Print the total points
print(f"\nTotal Points for All Cards: {total_points}")
