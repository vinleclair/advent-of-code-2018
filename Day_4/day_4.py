# SPAGHETTI CODE WARNING TURN BACK NOW YOU'VE BEEN WARNED

import re
import operator


def main():
    records = parse_input_file()
    guards = get_list_of_guards(records)
    sleepy_guard = get_sleepy_guard(guards, records)
    asleep_minute = find_most_asleep_minute(records, sleepy_guard)
    for x in list(guards.keys()):
        if guards[x] == 0:
            del guards[x]
    for guard in guards:
        guards[guard] = {}
    print("---Puzzle Answers---")
    print("Part 1:", asleep_minute * int(sleepy_guard.replace("#","")))
    print("Part 2:", find_sleepiest_minute(guards, records))


def find_sleepiest_minute(guards, records):
    most_frequent_minute = 0
    most_sleepy_minute = 0
    for guard in guards:
        guards[guard][find_most_asleep_minute(records, guard)] = find_asleep_frequency(records, guard)
    for guard in guards:
        if max(guards[guard].values()) > most_frequent_minute:
            most_frequent_minute = max(guards[guard].values())
            most_sleepy_minute = max(guards[guard].keys())
            guard_id = guard
    return int(guard_id.replace("#","")) * most_sleepy_minute


def find_asleep_frequency(records, sleepy_guard):
    sleepy_minutes = {}

    for index, record in enumerate(records):
        if len(re.findall(sleepy_guard, record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0:
            for minute in range(int(re.findall('\:\d+', records[index + 1])[0].replace(":","")), int(re.findall('\:\d+', records[index + 2])[0].replace(":",""))):
                if minute not in sleepy_minutes:
                    sleepy_minutes[minute] = 0
                elif minute in sleepy_minutes:
                    sleepy_minutes[minute] += 1

        if len(re.findall(sleepy_guard, record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0 and len(re.findall('falls asleep', records[index + 3])) > 0:
            for minute in range(int(re.findall('\:\d+', records[index + 3])[0].replace(":","")), int(re.findall('\:\d+', records[index + 4])[0].replace(":",""))):
                if minute not in sleepy_minutes:
                    sleepy_minutes[minute] = 0
                elif minute in sleepy_minutes:
                    sleepy_minutes[minute] += 1
    return max(sleepy_minutes.values())


def find_most_asleep_minute(records, sleepy_guard):
    sleepy_minutes = {}

    for index, record in enumerate(records):
        if len(re.findall(sleepy_guard, record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0:
            for minute in range(int(re.findall('\:\d+', records[index + 1])[0].replace(":","")), int(re.findall('\:\d+', records[index + 2])[0].replace(":",""))):
                if minute not in sleepy_minutes:
                    sleepy_minutes[minute] = 0
                elif minute in sleepy_minutes:
                    sleepy_minutes[minute] += 1

        if len(re.findall(sleepy_guard, record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0 and len(re.findall('falls asleep', records[index + 3])) > 0:
            for minute in range(int(re.findall('\:\d+', records[index + 3])[0].replace(":","")), int(re.findall('\:\d+', records[index + 4])[0].replace(":",""))):
                if minute not in sleepy_minutes:
                    sleepy_minutes[minute] = 0
                elif minute in sleepy_minutes:
                    sleepy_minutes[minute] += 1
    return max(sleepy_minutes.items(), key=operator.itemgetter(1))[0]


def get_sleepy_guard(guards, records):
    for index, record in enumerate(records):
        try:
            if len(re.findall('\#\d+', record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0:
                guards[re.findall('\#\d+', record)[0]] += int(re.findall('\:\d+', records[index + 2])[0].replace(":","")) - int(re.findall('\:\d+', records[index + 1])[0].replace(":",""))
            if len(re.findall('\#\d+', record)) > 0 and len(re.findall('falls asleep', records[index + 1])) > 0 and len(re.findall('falls asleep', records[index + 3])) > 0:
                guards[re.findall('\#\d+', record)[0]] += int(re.findall('\:\d+', records[index + 4])[0].replace(":","")) - int(re.findall('\:\d+', records[index + 3])[0].replace(":",""))
        except IndexError:
            print("GIMME A BREAK GIMMME A BREAK BREAK BREAK BREAK")
            break
    return max(guards.items(), key=operator.itemgetter(1))[0]


def get_list_of_guards(records):
    guards = {}

    for record in records:
        if len(re.findall('\#\d+', record)) > 0:
            guard = re.findall('\#\d+', record)[0]
            if guard not in records:
                guards[guard] = 0
    return guards


def parse_input_file():

    records = []
    try:
        with open(input("Name of input file: "), 'r') as file_pointer:
            for line in file_pointer:
                records.append(line)
    except FileNotFoundError:
        print("\nError: File not found.")
        exit(1)
    return sorted(records)


if __name__ == "__main__":
    main()
