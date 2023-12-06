def prepare(input_filename):
    cards = []

    with open(input_filename, 'r') as file:
        for line in file:
            winners, numbers = line.strip().split(': ')[1].split(' | ')
            cards.append((winners.split(), numbers.split()))

    return cards

def second(input): 
    cards = [1] * len(input)

    for (i, card) in enumerate(input):
        for j in range(i + 1, i + 1 + len(set(card[0]) & set(card[1]))):
            cards[j] += 1 * cards[i]

    return sum(cards)


# Replace 'input.txt' with the actual filename
input_filename = 'input.txt'
input_data = prepare(input_filename)

result_second = second(input_data)

print("Second Result:", result_second)
