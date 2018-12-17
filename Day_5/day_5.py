from string import *
EXTRA_CHARS = 2


def main():
    polymer = open('input.txt').read()
    print("---Puzzle Answers---")
    print("Part 1:", collapse(polymer))
    print("Part 2:", min(collapse(unit for unit in polymer if unit.lower() != letter) for letter in ascii_lowercase))


def collapse(polymer):
    new_polymer = ['']
    for current_unit in polymer:
        last_unit = new_polymer[-1]
        if last_unit != current_unit and last_unit.lower() == current_unit.lower():
            new_polymer.pop()
        else:
            new_polymer.append(current_unit)
    return len(new_polymer) - EXTRA_CHARS


if __name__ == "__main__":
    main()
