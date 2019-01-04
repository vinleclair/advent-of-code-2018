import fileinput


def main():
    tree = parse(map(int, next(fileinput.input()).split()))
    print("Part 1:", part_1(tree))


def part_1(node):
    metadata, children = node
    return sum(metadata) + sum(part_1(x) for x in children)


def parse(it):
    child_qty, metadata_qty = next(it), next(it)
    children = [parse(it) for _ in range(child_qty)]
    metadata = [next(it) for _ in range(metadata_qty)]

    return (metadata, children)

if __name__ == "__main__":
    main()
