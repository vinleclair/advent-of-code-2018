import itertools
import re
from collections import namedtuple


def main():
    claims = parse_input_file()
    empty_fabric = instantiate_empty_fabric(claims)
    fabric = populate_fabric(claims, empty_fabric)
    print("---Puzzle Answers---")
    print("Square inches of fabric:", sum( x == 2 for x in empty_fabric.values()))
    print("Claim #:", find_no_overlap(claims, fabric))
    return(1)


def parse_input_file():

    claims = []
    coordinates = {"#" : 0,
            "xmin" : 0,
            "ymin" : 0,
            "xmax" : 0,
            "ymax" : 0}
    try:
        with open(input("Name of input file: "), 'r') as file_pointer:
            for line in file_pointer:
                numbers = re.findall('\d+', line)
                coordinates["#"] = int(numbers[0])
                coordinates["xmin"] = int(numbers[1])
                coordinates["ymin"] = int(numbers[2])
                coordinates["xmax"] = int(numbers[1]) + int(numbers[3])
                coordinates["ymax"] = int(numbers[2]) + int(numbers[4])
                claims.append(coordinates.copy())
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)
    return claims


def instantiate_empty_fabric(claims):
    x_min = max(claims, key=lambda x: x["xmin"]).get("xmin")
    x_max = max(claims, key=lambda x: x["xmax"]).get("xmax")
    y_min = max(claims, key=lambda x: x["ymin"]).get("ymin")
    y_max = max(claims, key=lambda x: x["ymax"]).get("ymax")
    empty_fabric = {}

    for x_index, y_index in itertools.product(range(x_max), range(y_max)):
        empty_fabric[x_index, y_index] = 0
    return empty_fabric


def populate_fabric(claims, empty_fabric):
    for claim in claims:
        x_start = claim.get("xmin")
        x_end = claim.get("xmax")
        y_start = claim.get("ymin")
        y_end = claim.get("ymax")
        for x, y in itertools.product(range(x_start, x_end), range(y_start, y_end)):
            if empty_fabric[x, y] == 0 or empty_fabric[x, y] == 1:
                empty_fabric[x, y] += 1
    return empty_fabric


def find_no_overlap(claims, fabric):
    for claim in claims:
        x_start = claim.get("xmin")
        x_end = claim.get("xmax")
        y_start = claim.get("ymin")
        y_end = claim.get("ymax")
        size = (x_end - x_start) * (y_end - y_start)
        squares = 0
        for x, y in itertools.product(range(x_start, x_end), range(y_start, y_end)):
            if fabric[x, y] == 1:
                squares += 1
                if squares == size:
                    return claim.get("#")
    return


if __name__ == "__main__":
    main()

