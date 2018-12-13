def main():

    frequencies = parse_input_file()
    current_frequency = 0
    past_frequencies = []
    calibrating = True

    print("\nCalibrating...")
    while calibrating:
        for frequency in frequencies:
            current_frequency += frequency

            if current_frequency in past_frequencies:
                calibrating = False
                break

            past_frequencies.append(current_frequency)

    print("--- Puzzle Answers ---")
    print("Part 1 :", sum(frequencies))
    print("Part 2 :", current_frequency)


def find_letters_in_common(box_ids):
    i = 0
    j = 1
    while i < len(box_ids):
        while j < len(box_ids):
            count_diffs = 0
            for a, b in zip(box_ids[i], box_ids[j]):
                if a!=b:
                    count_diffs += 1
                print("Word #:",i,j, "Differences :", count_diffs)
                if count_diffs == 1:
                    first_word = box_ids[i]
                    second_word = box_ids[j]
                j += 1
        i += 1
        print("yo")


def parse_input_file():

    frequencies = []
    try:
        with open(input("Name of input file: "), 'r') as fp:
            for line in fp:
                frequencies.append(int(line))
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)

    return frequencies


if __name__ == "__main__":
    main()
