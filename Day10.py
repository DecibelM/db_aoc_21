from input import Imports

importClass = Imports()


class Day10:
    @staticmethod
    def task1():
        # inp = importClass.getInput("input/input10_test.txt")
        inp = importClass.getInput("input/input10.txt")

        wrong_lines = []
        wrong_lines_index = []
        sum = 0
        for i in range(0, len(inp)):
            line = inp[i]
            score = Day10.check_line(line)
            wrong_lines.append(score)
            if score > 0:
                wrong_lines_index.append(line)
            sum += score

        for line in wrong_lines_index:
            inp.remove(line)

        print(sum)
        return inp

    @staticmethod
    def task2(inp):
        result = []
        for input_line in inp:

            remaining = Day10.complete_line(input_line)
            complete_with = Day10.get_completed(remaining)
            print(complete_with)
            sum = 0
            for item in complete_with:
                sum *= 5
                sum += Day10.get_completion_points(item)
            result.append(sum)
        print(result)
        result.sort()
        print(result)
        middle = len(inp) / 2 - 0.5
        print(middle)
        print(result[int(middle)])

    @staticmethod
    def get_completed(input_line):
        completed = []
        for char in reversed(input_line):
            completed.append(Day10.find_matching(char))
        return completed

    @staticmethod
    def get_points(char):
        if char == ">":
            return 25137
        elif char == ")":
            return 3
        elif char == "}":
            return 1197
        elif char == "]":
            return 57

    @staticmethod
    def get_completion_points(char):
        if char == ">":
            return 4
        elif char == ")":
            return 1
        elif char == "}":
            return 3
        elif char == "]":
            return 2

    @staticmethod
    def complete_line(input_line):
        characters = []
        next_closing = []

        for char in input_line:
            if char == "<" or char == "(" or char == "{" or char == "[":
                characters.append(char)
                next_closing.append(Day10.find_matching(char))
            else:
                next = next_closing.pop()
                if next != char:
                    print(f"Line is wrong")
                    return Day10.get_points(char)
                else:
                    characters.pop()

        return characters

    @staticmethod
    def check_line(input_line):
        characters = []
        next_closing = []

        for char in input_line:
            if char == "<" or char == "(" or char == "{" or char == "[":
                characters.append(char)
                next_closing.append(Day10.find_matching(char))
            else:
                next = next_closing.pop()
                if next != char:
                    print(f"Line is wrong")
                    return Day10.get_points(char)

        return 0

    @staticmethod
    def find_matching(char):
        if char == "<":
            return ">"
        elif char == "(":
            return ")"
        elif char == "{":
            return "}"
        elif char == "[":
            return "]"
