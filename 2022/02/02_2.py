import sys
import fileinput

'''
python 02_2.py input_02.txt

Input legend:
    A: Rock         X: Need LOSS
    B: Paper        Y: Need DRAW
    C: Scissors     Z: Need WIN

Scoring rules:
    Rock:       1       Loss:   0
    Paper:      2       Draw:   3
    Scissors:   3       Win:    6

Calculate score for yourself (player_2)
'''

#FIXME these data structures are terrible
MOVES = {
            "rock": ("A", 1),
            "paper": ("B", 2),
            "scissors": ("C", 3)
        }

OUTCOMES = {
            "loss": ("X", 0),
            "draw": ("Y", 3),
            "win": ("Z", 6)
        }

def parse_move(enc_move):
    move = ''
    pts = 0
    for k,v in MOVES.items():
        if enc_move == v[0]:
            move = k
            pts = v[1]
            break
    return move, pts

def parse_outcome(enc_outcome):
    outcome = ''
    for k,v in OUTCOMES.items():
        if enc_outcome == v[0]:
            outcome = k
            break
    return outcome

def get_round_score(input_1, input_2):
    score = 0
    move_1, pts_1 = parse_move(input_1)
    outcome = parse_outcome(input_2)

    match outcome:
        case "loss":
            score += OUTCOMES["loss"][1] + (MOVES["scissors"][1] if move_1 == "rock" else MOVES["rock"][1] if move_1 == "paper" else MOVES["paper"][1])
        case "draw":
            score += OUTCOMES["draw"][1] + (MOVES["rock"][1] if move_1 == "rock" else MOVES["paper"][1] if move_1 == "paper" else MOVES["scissors"][1])
        case "win":
            score += OUTCOMES["win"][1] + (MOVES["paper"][1] if move_1 == "rock" else MOVES["scissors"][1] if move_1 == "paper" else MOVES["rock"][1])
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

    assert result == 11998
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
