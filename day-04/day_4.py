from collections import defaultdict


def main():
    records = open_input_file()
    most_asleep_minute, guard_sleep_minutes = get_time_dicts(records)
    print("---Puzzle Answers---")
    print("Part 1:", arg_max(guard_sleep_minutes) * arg_max_minute(most_asleep_minute, arg_max(guard_sleep_minutes)))
    print("Part 2:", arg_max(most_asleep_minute)[0] * arg_max(most_asleep_minute)[1])


def get_time_dicts(records):
    guard_sleep_minutes = defaultdict(int)
    most_asleep_minute = defaultdict(int)
    guard = None
    asleep = None
    for line in records:
        if line:
            time = parse_time(line)
            if 'begins shift' in line:
                guard = int(line.split()[3][1:])
                asleep = None
            elif 'falls asleep' in line:
                asleep = time
            elif 'wakes up' in line:
                for minute in range(asleep, time):
                    most_asleep_minute[(guard, minute)] += 1
                    guard_sleep_minutes[guard] += 1
    return most_asleep_minute, guard_sleep_minutes


def arg_max(dictionary):
    best = None
    for key,value in dictionary.items():
        if best is None or value > dictionary[best]:
            best = key
    return best


def arg_max_minute(dictionary, guard):
    best = None
    for key,value in dictionary.items():
        if (best is None or value > dictionary[best]) and key[0] == guard:
            best = key
    return best[1]


def parse_time(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def open_input_file():

    records = open('input.txt').read().split('\n')
    return sorted(records)


if __name__ == "__main__":
    main()
