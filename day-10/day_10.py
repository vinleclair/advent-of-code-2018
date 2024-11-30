import re
import fileinput

def main():
    points  = parse_input()
    stars, time = align_stars(points)
    print(display(stars))
    print("Part 2:", time)


def align_stars(points):
    area = []
    time = 0
    while True:
        for point in points:
            point[0] += point[2]
            point[1] += point[3]
        box = find_bounding_box(points)
        area.append(calc_area(box))
        #if the area is suddenly increasing, revert the last changes and break
        if len(area) > 1 and area[-1] > area[-2]:
            for point in points:
                point[0] -= point[2] * 2
                point[1] -= point[3] * 2
            time -= 1
            break
        time += 1
    return points, time


def find_bounding_box(points):
    bot_left_x, bot_left_y = float('inf'), float('inf')
    top_right_x, top_right_y = float('-inf'), float('-inf')
    for x, y, _, _ in points:
        bot_left_x = min(bot_left_x, x)
        bot_left_y = min(bot_left_y, y)
        top_right_x = max(top_right_x, x)
        top_right_y = max(top_right_y, y)

    return (bot_left_x, bot_left_y, top_right_x, top_right_y)


def calc_area(box):
    return (abs(box[0]) + abs(box[2])) * (abs(box[1]) + abs(box[3]))


def display(points):
    x0, y0, x1, y1 = find_bounding_box(points)
    rows = []
    star = False
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            for point in points:
                if x == point[0] and y == point[1]:
                    row.append('*')
                    star = True
                    break
            if star == False:
                row.append(' ')
            else:
                star = False
        rows.append(''.join(row))
    return '\n'.join(rows)

def parse_input():
    return [list(map(int, re.findall(r'\-?\d+', line))) for line in fileinput.input()]


if __name__ == "__main__":
    main()
