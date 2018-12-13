import itertools


def main():
    box_ids = parse_input_file()
    print("--- Puzzle Answers ---")
    print("Checksum :", find_checksum(box_ids))
    print("Letters in common:", find_letters_in_common(box_ids))
    return 0


def find_checksum(box_ids):

    letter_count = {"doubles" : 0,
                    "triples" : 0}

    for box_id in box_ids:
        counted_double = False
        counted_triple = False
        for letter in box_id:
            if box_id.count(letter) == 2 and not counted_double:
                letter_count["doubles"] += 1
                counted_double = True
            elif box_id.count(letter) == 3 and not counted_triple:
                letter_count["triples"] += 1
                counted_triple = True

    return letter_count["doubles"] * letter_count["triples"]


def find_letters_in_common(box_ids):
    for box_id_one, box_id_two in itertools.combinations(box_ids, 2):
        if count_differences(box_id_one, box_id_two) == 1:
            for first_letter, second_letter in zip(box_id_one, box_id_two):
                if first_letter != second_letter:
                    letters_in_common = box_id_one.replace(first_letter, "")
    return letters_in_common


def count_differences(first_string, second_string):
    count_diffs = 0
    for first_letter, second_letter in zip(first_string, second_string):
        if first_letter != second_letter:
            count_diffs += 1
    return count_diffs


def parse_input_file():

    box_ids = []
    try:
        with open(input("Name of input file: "), 'r') as file_pointer:
            for line in file_pointer:
                box_ids.append(line.rstrip())
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)

    return box_ids


if __name__ == "__main__":
    main()
