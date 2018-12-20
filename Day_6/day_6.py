from collections import defaultdict
import fileinput
import re


def main():
    coordinates = parse_input_file()
    x_min, x_max = min(x for x, y in coordinates), max(x for x, y in coordinates)
    y_min, y_max = min(y for x, y in coordinates), max(y for x, y in coordinates)
    print("---Puzzle Answers---")
    print("Part 1:", max(part_1(coordinates, x_min, x_max, y_min, y_max).values()))
    print("Part 2:", part_2(coordinates, x_min, x_max, y_min, y_max))


def part_1(coordinates, x_min, x_max, y_min, y_max):
    counts = defaultdict(int)
    infinite = set()

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            distance = sorted((manhattan_distance(x, px, y, py), point_index) for point_index, (px, py) in enumerate(coordinates))
            if distance[0][0] != distance[1][0]:
                counts[distance[0][1]] += 1
                if x == x_min or x == x_max or y == y_min or y == y_max:
                    infinite.add(distance[0][1])
    for k in infinite:
        counts.pop(k)
    return counts


def part_2(coordinates, x_min, x_max, y_min, y_max):
    count = 0

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if sum(manhattan_distance(x, px, y, py) for px, py in coordinates) < 10000:
                count += 1

    return count


def manhattan_distance(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def parse_input_file():
    return [tuple(map(int, re.findall(r'\d+', line))) for line in fileinput.input()]


if __name__ == "__main__":
    main()
