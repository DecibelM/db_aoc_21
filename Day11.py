from input import Imports

importClass = Imports()


class Day11:
    @staticmethod
    def task1():
        # inp = importClass.getInput("input/input11_test.txt")
        inp = importClass.getInput("input/input11.txt")
        inp = list(map(lambda row: list(row), inp))
        steps = 100

        for i in range(0, len(inp)):
            inp[i] = list(map(lambda item: int(item), inp[i]))

        Day11.print_map(inp)
        sum_flashes = 0
        step = 1
        while not Day11.is_zero(inp):
            flashes = Day11.increase_energy(inp)
            sum_flashes += len(flashes)
            if len(flashes) > 0:
                while len(flashes) > 0:
                    flashes = Day11.flash(inp, flashes)
                    sum_flashes += len(flashes)
            if step == steps:
                task1_res = sum_flashes
            step += 1

        Day11.print_map(inp)
        print(f"Task1: {task1_res}")
        print(f"Task2: {step-1}")

    @staticmethod
    def is_zero(inp):
        for row in inp:
            for item in row:
                if item != 0:
                    return False
        return True

    @staticmethod
    def flash(inp, flashes):
        new_flashes = []
        for ij in flashes:
            i_range = Day11.get_range(ij[0], len(inp))
            j_range = Day11.get_range(ij[1], len(inp[0]))
            i_min = ij[0] + i_range[0]
            i_max = ij[0] + i_range[-1]
            j_min = ij[1] + j_range[0]
            j_max = ij[1] + j_range[-1]

            for i in range(i_min, i_max + 1):
                for j in range(j_min, j_max + 1):
                    if not (i == ij[0] and j == ij[1]) and inp[i][j] != 0:
                        inp[i][j] += 1
                    if inp[i][j] > 9:
                        new_flashes.append([i, j])
                        inp[i][j] = 0
        return new_flashes

    @staticmethod
    def get_range(index, length):
        if index == 0:
            i_range = [0, 1]
        elif index == (length - 1):
            i_range = [-1, 0]
        else:
            i_range = [-1, 0, 1]
        return i_range

    @staticmethod
    def increase_energy(inp):
        flashes = []
        for i in range(0, len(inp)):
            for j in range(0, len(inp[0])):
                inp[i][j] += 1
                if inp[i][j] > 9:
                    flashes.append([i, j])
                    inp[i][j] = 0
        return flashes

    @staticmethod
    def print_map(inp):
        [print(row) for row in inp]
        print("------------------------------")
