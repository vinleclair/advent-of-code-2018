import fileinput
import re


def main():
    num_players, last_marble = parse_input()
    print("Players:", num_players)
    print("Marbles:", last_marble)


def parse_input():
    num_players, last_marble = map(int, re.findall(r'\d+', next(fileinput.input())))
    return (num_players, last_marble)


if __name__ == "__main__":
    main()
