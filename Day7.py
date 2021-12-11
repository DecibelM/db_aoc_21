from collections import Counter
from input import Imports
import time

importClass = Imports()


class Day7:
    @staticmethod
    def task1():
        # inp = importClass.getInput_split_by_comma("input/input7_test.txt")
        inp = importClass.getInput_split_by_comma("input/input7.txt")

        counter = Counter(inp)
        keys = counter.keys()
        lowest_fuel = 10000000000000
        lowest_key = 0

        for key in keys:
            fuel = 0
            for fish in inp:
                fuel += abs(fish - key)

            if fuel < lowest_fuel:
                lowest_fuel = fuel
                lowest_key = key

        print(f"Baseline: {lowest_key}, lowest fuel: {lowest_fuel}")

    @staticmethod
    def task2():
        start_time = time.time()
        # inp = importClass.getInput_split_by_comma("input/input7_test.txt")
        inp = importClass.getInput_split_by_comma("input/input7.txt")

        counter = Counter(inp)
        keys = counter.keys()
        start = 1000000
        stop = 0
        for key in keys:
            if key < start:
                start = key
            if key > stop:
                stop = key

        lowest_fuel = 10000000000000
        lowest_key = 0

        for i in range(start, stop + 1):
            fuel = 0
            for fish in inp:
                n = abs(fish - i)
                fuel += n * (n + 1) / 2

            if fuel < lowest_fuel:
                lowest_fuel = fuel
                lowest_key = i

        print(f"Baseline: {lowest_key}, lowest fuel: {lowest_fuel}")
        print(f"Time: {time.time() - start_time}")
