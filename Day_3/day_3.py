import itertools
import re
from collections import namedtuple

def main():
    claims = parse_input_file()
    print(find_total_overlap(claims))

def find_total_overlap(claims):
    total_overlap = 0
    for rectangle_one, rectangle_two in itertools.combinations(claims, 2):
        total_overlap += overlap_area(rectangle_one, rectangle_two)
    return total_overlap


def overlap_area(rectangle_one, rectangle_two):  # returns None if rectangles don't intersect
    dx = min(rectangle_one["xmax"], rectangle_two["xmax"]) - max(rectangle_one["xmin"], rectangle_two["xmin"])
    dy = min(rectangle_one["ymax"], rectangle_two["ymax"]) - max(rectangle_one["ymin"], rectangle_two["ymin"])
    if (dx>=0) and (dy>=0):
        return dx*dy


def parse_input_file():

    claims = []
    coordinates = {"xmin" : 0,
            "ymin" : 0,
            "xmax" : 0,
            "ymax" : 0}
    try:
        with open(input("Name of input file: "), 'r') as file_pointer:
            for line in file_pointer:
                numbers = re.findall('\d+', line)
                coordinates["xmin"] = int(numbers[1])
                coordinates["ymin"] = int(numbers[2])
                coordinates["xmax"] = int(numbers[1]) + int(numbers[3])
                coordinates["ymax"] = int(numbers[2]) + int(numbers[4])
                claims.append(coordinates)
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)
    return claims

if __name__ == "__main__":
    main()

