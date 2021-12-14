from collections import Counter

from input import Imports

importClass = Imports()


def polymer_insertion(polymer, rules):
    n = 0
    while n + 1 < len(polymer):
        polymer_pair = polymer[n : n + 2]
        insertion = rules[polymer_pair]
        first_part = polymer[: n + 1]
        second_part = polymer[n + 1 :]
        polymer = first_part + insertion + second_part
        n += 2
    return polymer


def insert_pair(pair, polymer_pairs, n):
    if pair not in polymer_pairs:
        polymer_pairs[pair] = n
    else:
        polymer_pairs[pair] += n
    return polymer_pairs


def polymer_insertion2(polymer_pairs, rules):
    new_polymer_pairs = {}
    for pair in polymer_pairs:
        insertion = rules[pair]
        new_pair_1 = pair[0] + insertion
        new_pair_2 = insertion + pair[1]
        new_polymer_pairs = insert_pair(
            new_pair_1, new_polymer_pairs, polymer_pairs[pair]
        )
        new_polymer_pairs = insert_pair(
            new_pair_2, new_polymer_pairs, polymer_pairs[pair]
        )

    return new_polymer_pairs


def count_occurences(pairs, polymer_first, polymer_last):
    occurences = {}
    for pair in pairs:
        pair_counter = dict(Counter(pair))

        for item in pair_counter:
            if item not in occurences:
                occurences[item] = pair_counter[item] * pairs[pair]
            else:
                occurences[item] += pair_counter[item] * pairs[pair]
    print(occurences)
    for item in occurences:
        if item == polymer_first or item == polymer_last:
            occurences[item] = (occurences[item] - 1) / 2 + 1
        else:
            occurences[item] = occurences[item] / 2
    return occurences


class Day14:
    @staticmethod
    def task1():
        # inp = importClass.getInput("input/input14_test.txt")
        inp = importClass.getInput("input/input14.txt")

        polymer = inp.pop(0)
        inp.pop(0)

        rules = dict(map(lambda row: row.split(" -> "), inp))
        polymer_pairs = {}
        n = 0
        while n < len(polymer) - 1:
            polymer_pair = polymer[n : n + 2]
            insert_pair(polymer_pair, polymer_pairs, 1)
            n += 1

        for i in range(0, 40):
            polymer_pairs = polymer_insertion2(polymer_pairs, rules)
            print(sum(polymer_pairs.values()))

        occurrences = count_occurences(polymer_pairs, polymer[0], polymer[-1])
        occurrences_counter = list(Counter(occurrences).most_common())

        print(polymer_pairs)
        print(occurrences)
        most_common = occurrences_counter[0]
        least_common = occurrences_counter[-1]
        print((most_common[1] - least_common[1]))
