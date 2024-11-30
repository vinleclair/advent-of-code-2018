import fileinput


def main():
    tree = parse(map(int, next(fileinput.input()).split()))
    metadata, children = tree
    print("Part 1:", part_1(tree))
    print("Part 2:", part_2(tree))

def part_1(node):
    metadata, children = node
    return sum(metadata) + sum(part_1(x) for x in children)


def part_2(node):
    metadata, children = node
    if children:
        return sum(part_2(children[i-1]) for i in metadata if 1 <= i <= len(children))
    return sum(metadata)


def parse(it):
    child_qty, metadata_qty = next(it), next(it)

    children = [parse(it) for _ in range(child_qty)]
    metadata = [next(it) for _ in range(metadata_qty)]

    return (metadata, children)

if __name__ == "__main__":
    main()
