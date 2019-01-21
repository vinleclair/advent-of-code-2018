from collections import defaultdict
import fileinput


def main():
    grid = initialize_summed_area_table(int(next(fileinput.input())))
    print('Part 1: %d,%d' % find_max_power(grid, 3)[1:])
    print('Part 2: %d,%d,%d' % max(find_max_power(grid, size) + (size,) for size in range(1, 301))[1:])


def find_max_power(grid, size):
    power = []
    for y in range(1, 301 - size + 1):
        for x in range(1, 301 - size + 1):
            region = calculate_region(grid, size, x, y)
            power.append((region, x, y))
    return max(power)


def calculate_region(grid, size, x, y):
    x0, y0, x1, y1 = x - 1, y - 1, x + size - 1, y + size - 1
    return grid[(x0, y0)] + grid[(x1, y1)] - grid[(x1, y0)] - grid[(x0, y1)]


def initialize_summed_area_table(serial_number):
    grid = defaultdict(int)
    for y in range(1, 301):
        for x in range(1, 301):
            rack_id = x + 10
            power_level = (((rack_id * y + serial_number) * rack_id) // 100) % 10 - 5
            grid[(x,y)] = power_level + grid[(x, y - 1)] + grid[(x - 1, y)] - grid[(x - 1, y - 1)]
    return grid

if __name__ == "__main__":
    main()
