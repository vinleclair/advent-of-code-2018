import fileinput
import re


def main():
    license = parse_input_file()
    return 0


def parse_input_file():
    for number in fileinput.input():
        return list(map(int,re.findall(r'\d+', number)))


if __name__ == "__main__":
    main()
