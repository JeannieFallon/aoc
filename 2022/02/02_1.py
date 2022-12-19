import sys
import fileinput

'''
python 02_1.py input_02.txt

Input legend:
    A, X: Rock
    B, Y: Paper
    C, Z: Scissors

Scoring rules:
    Rock:       1       Loss:   0
    Paper:      2       Draw:   3
    Scissors:   3       Win:    6

Calculate score for yourself (player_2)
'''

LOSS = 0
DRAW = 3
WIN = 6

LEGEND = {
            "rock": [("A", "X"), 1],
            "paper": [("B", "Y"), 2],
            "scissors": [("C", "Z"), 3]
        }

def parse_move(enc_move):
    move = ''
    pts = 0
    for k,v in LEGEND.items():
        if enc_move in v[0]:
            move = k
            pts = v[1]
            break
    return move, pts

def get_round_score(player_1, player_2):
    move_1, pts_1 = parse_move(player_1)
    move_2, pts_2 = parse_move(player_2)

    score = pts_2
    if move_1 == move_2:
        score += DRAW
    else:
        match move_1:
            case 'rock':
                score += WIN if move_2 == 'paper' else LOSS
            case 'paper':
                score += WIN if move_2 == 'scissors' else LOSS
            case 'scissors':
                score += WIN if move_2 == 'rock' else LOSS
            case _:
                raise

    return score


def get_total_score():
    total_score = 0

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            total_score += get_round_score(line[0], line[2])

    return total_score


def main():
    result = get_total_score()

    assert result == 8933
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
