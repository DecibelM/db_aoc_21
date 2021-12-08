from collections import Counter
from input import Imports
import time

importClass = Imports()


class Day8:

    @staticmethod
    def task1():
        #inp = importClass.getInput("input/input8_test.txt")
        inp = importClass.getInput("input/input8.txt")

        for i in range(0, len(inp)):
            inp[i] = inp[i].split('|')
            inp[i][1] = inp[i][1].split()

        sum = 0

        for i in range(0, len(inp)):
            for item in inp[i][1]:
                if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
                    sum+= 1


        print(f"Task1: {sum}")

    @staticmethod
    def task2():
        #inp = importClass.getInput("input/input8_test_2.txt")
        inp = importClass.getInput("input/input8.txt")

        for i in range(0, len(inp)):
            inp[i] = inp[i].split('|')
            inp[i][1] = inp[i][1].split()
            inp[i][0] = inp[i][0].split()
        sum = 0
        for thing in inp:
            code = Day8.task2_exec(thing[0])
            number = ""
            for dsfs in thing[1]:
                sorted_dfds = ''.join(sorted(dsfs))
                decoded = code[sorted_dfds]
                number = number + str(decoded)
            sum += int(number)
        print(f"Task2: {sum}")


    @staticmethod
    def task2_exec(inp):

        numbers = {}
        wires = {}
        list = inp
        for item in list:
            if len(item) == 2:
                numbers[1] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 1
            elif len(item) == 4:
                numbers[4] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 4
            elif len(item) == 3:
                numbers[7] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 7
            elif len(item) == 7:
                numbers[8] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 8

        list.remove(numbers[1])
        list.remove(numbers[4])
        list.remove(numbers[7])
        list.remove(numbers[8])

        for item in list:
            item_set = set(item)
            set_seven = set(numbers[7])
            is_in = set_seven.issubset(item_set)
            if len(item) == 6 and (not is_in):
                numbers[6] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 6
                break
        list.remove(numbers[6])

        for item in list:
            item_set = set(item)
            set_six = set(numbers[6])
            set_seven = set(numbers[7])
            is_in_7 = set_seven.issubset(item)
            is_in = item_set.issubset(set_six)
            if len(item) == 5 and is_in_7:
                numbers[3] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 3
                break
        list.remove(numbers[3])

        for item in list:
            item_set = set(item)
            set_six = set(numbers[6])
            is_in = item_set.issubset(set_six)
            if len(item) == 5 and is_in:
                numbers[5] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 5
            elif len(item) == 5 and (not is_in):
                numbers[2] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 2
        list.remove(numbers[5])
        list.remove(numbers[2])


        for item in list:
            item_set = set(item)
            set_five = set(numbers[5])
            set_six = set(numbers[6])
            is_in = item_set.issubset(set_six)
            is_in_five = set_five.issubset(item)
            if len(item) == 6 and is_in_five:
                numbers[9] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 9
            elif len(item) == 6 and (not is_in_five):
                numbers[0] = item
                sorted_item = ''.join(sorted(item))
                wires[sorted_item] = 0

        print(numbers)
        print(wires)
        return wires



