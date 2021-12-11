from collections import Counter
from input import Imports

importClass = Imports()


class Day6:
    @staticmethod
    def task1():
        inp = importClass.getInput_split_by_comma("input/input6_test.txt")
        # inp = importClass.getInput_split_by_comma("input/input6.txt")
        no_of_days = 80

        fish_count = dict(Counter(inp))

        while no_of_days > 0:
            new_fish_count = {}
            for i in range(0, 9):
                if i == 0:
                    new_fish_count[8] = fish_count.get(0, 0)
                    new_fish_count[6] = fish_count.get(0, 0)
                elif i > 0:
                    new_fish_count[i - 1] = new_fish_count.get(
                        i - 1, 0
                    ) + fish_count.get(i, 0)

            fish_count = new_fish_count
            no_of_days -= 1

        print(sum(fish_count.values()))
