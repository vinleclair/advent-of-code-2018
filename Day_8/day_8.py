import fileinput
import re


def main():
    license = parse_input_file()
    print(part_1(license))
    return 0


def part_1(license):
    cursor = 0
    child_nodes_qty = 0
    metadata_quantity = 0
    total = 0
    for index, number in enumerate(license):
        if cursor == 0:
            child_nodes_qty = license[index]
            metadata_qty = license[index + 1]
            cursor = child_nodes_qty + 2
            for range_index in range(metadata_qty):
                print(license[range_index])
                total += license[range_index]
                cursor += 1
            index = cursor
        else:
            cursor = 0
        if index > len(license):
            break

    return total
        


def parse_input_file():
    for number in fileinput.input():
        return list(map(int,re.findall(r'\d+', number)))


if __name__ == "__main__":
    main()
