def main():

    ids_list = parse_input_file()
    counting = True
    letter_count = {"doubles" : 0,
                    "triples" : 0}
    for box_id in ids_list:
        counted_double = False
        counted_triple = False
        for letter in box_id:
            if box_id.count(letter) == 2 and not counted_double:
                letter_count["doubles"] += 1
                counted_double = True
            elif box_id.count(letter) == 3 and not counted_triple:
                letter_count["triples"] += 1
                counted_triple = True

    print("Checksum :",letter_count["doubles"] * letter_count["triples"])

    return 0


def parse_input_file():

    box_ids = []
    try:
        with open(input("Name of input file: "), 'r') as fp:
            for line in fp:
                box_ids.append(line.rstrip())
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)

    return box_ids


if __name__ == "__main__":
    main()
