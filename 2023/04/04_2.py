import sys
import fileinput

'''
python 04_2.py input_04.txt
'''


def get_total_cards(cards: list) -> int:
    _sum = 0
    copies = []

    # Get number of hits on each card
    for i, card in enumerate(cards):

        # Track copies by [card num, num hits, num copies]
        copy = [i+1, 0, 1]

        # Iterate over nums and check if in wins list
        for num in card[1]:
            if num in card[0]:
                copy[1] += 1

        copies.append(copy)
    print(copies)

    # Now get num copies based upon other cards
    for j, copy in enumerate(copies):
        # Get number of cards to increment
        hits = copy[1]

        # Get number of copies
        num_copies = copy[2]

        # Increment num copies for the following cards
        for num in range(num_copies):
            for k in range(hits):
                copies[j+k+1][2] += 1

        _sum += copy[2]

    return _sum


def main():
    result = 0

    # Create list of tuples to hold (winning nums, nums you have)
    cards = []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            # Parse each line into lists of winning nums and nums you have
            wins, nums = line.split('|')
            wins = [int(w) for w in wins.split(':')[1].strip().split()]
            nums = [int(n) for n in nums.strip().split()]

            #FIXME parse wins & nums and create the copies data struct here
            cards.append((wins, nums))

    # Need to get total after all cards have been parsed
    result += get_total_cards(cards)

    '''
    # Demo
    assert result == 30
    '''
    # Final
    assert result == 13080971

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
