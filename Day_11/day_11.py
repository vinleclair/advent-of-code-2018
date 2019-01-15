from collections import defaultdict
import fileinput

def main():
    grid = initialize_summed_area_table(int(next(fileinput.input())))
    print(grid)


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
