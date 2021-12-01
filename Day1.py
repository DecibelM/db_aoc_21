from input import Imports

importClass = Imports()


class Day1:

    @staticmethod
    def task_1():
        data = importClass.getInput("input/input_1.txt")
        counter = 0
        for i in range(1, len(data)):
            previous = int(data[i-1])
            current = int(data[i])
            if current > previous:
                counter += 1

        print("Part 1:" + counter)

    @staticmethod
    def task_2():
        data = importClass.getInput("input/input_1.txt")
        counter = 0
        for i in range(3, len(data)):
            sumA = int(data[i - 3]) + int(data[i - 2]) + int(data[i - 1])
            sumB = int(data[i - 2]) + int(data[i - 1]) + int(data[i])
            if sumB > sumA:
                counter += 1

        print("Part 1:" + counter)
