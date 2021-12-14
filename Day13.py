from input import Imports

importClass = Imports()


def fold(inp, instruction):
    instruction = instruction.split(" ")
    instruction = instruction[2].split("=")
    if instruction[0] == "y":
        direction = 1
    else:
        direction = 0
    instruction = int(instruction[1])

    new_points = []
    folded_points = []

    for point in inp:
        if point[direction] > instruction:
            folded_points.append(point)
            point[direction] = point[direction] - 2 * (point[direction] - instruction)
            new_points.append(point)
        elif point == instruction:
            folded_points.append(point)

    for p in folded_points:
        inp.remove(p)

    inp.extend([e for e in new_points if e not in inp])
    return inp


def print_map(points):
    x_max = max(map(lambda e: e[0], points))
    y_max = max(map(lambda e: e[1], points))

    points_map = []
    for i in range(0, x_max + 1):
        points_map.append([])
        for j in range(0, y_max + 1):
            points_map[i] += " "

    for point in points:
        points_map[point[0]][point[1]] = "X"

    for row in points_map:
        print(row)


class Day13:
    @staticmethod
    def task1():
        # inp = importClass.getInput("input/input13_test.txt")
        inp = importClass.getInput("input/input13.txt")

        instructions = []
        next = inp.pop()
        while next != "":
            instructions.append(next)
            next = inp.pop()

        inp = list(map(lambda row: row.split(","), inp))
        for row in inp:
            row[0] = int(row[0])
            row[1] = int(row[1])

        while len(instructions) > 0:
            inp = fold(inp, instructions.pop())

        no_points = len(inp)

        print(inp)
        print(no_points)
        print_map(inp)
