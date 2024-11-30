from collections import deque
import fileinput
import re


def main():
    num_players, last_marble = parse_input()
    print("Part 1:", marble_game(num_players, last_marble))
    print("Part 2:", marble_game(num_players, last_marble * 100))


def marble_game(num_players, last_marble):
    circle = deque([0])
    scores = [0] * num_players
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % num_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)


def parse_input():
    num_players, last_marble = map(int, re.findall(r'\d+', next(fileinput.input())))
    return (num_players, last_marble)


if __name__ == "__main__":
    main()
