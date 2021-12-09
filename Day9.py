from input import Imports

importClass = Imports()


class Point:

    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value


class Day9:

    @staticmethod
    def input():
        # inp = importClass.getInput("input/input9_test.txt")
        inp = importClass.getInput("input/input9.txt")
        inp_map = map(lambda row: list(row), inp)
        inp = list(inp_map)
        return inp

    @staticmethod
    def task1():
        inp = Day9.input()
        low_points = []

        for i in range(0, len(inp)):
            for j in range(0, len(inp[i])):
                item = inp[i][j]
                is_low = Day9.is_low_point(inp, i, j)
                if is_low:
                    low_points.append(Point(i, j, int(item)))

        sum = 0
        for item in low_points:
            sum += item.value + 1
        print(f"Task1: {sum}")
        return low_points

    @staticmethod
    def is_low_point(inp, i, j):
        item = int(inp[i][j])
        i_range = Day9.get_range(i, len(inp))
        j_range = Day9.get_range(j, len(inp[i]))
        for k in i_range:
            for n in j_range:
                neighbor = int(inp[i + k][j + n])
                neighbor_is_smaller = (neighbor <= item)
                if neighbor_is_smaller and (k != 0 or n != 0):
                    return False
        return True

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
    def task2(low_points):
        inp = Day9.input()
        sizes = []
        for low_point in low_points:
            sizes.append(Day9.search(inp, low_point))

        sizes.sort(reverse=True)
        print(f"Task2: {sizes[0] * sizes[1] * sizes[2]}")

    @staticmethod
    def search(inp, low_point):
        visited = set()

        def find_neighbors(node):
            neighbors = []
            i_range = Day9.get_range(node.i, len(inp))
            j_range = Day9.get_range(node.j, len(inp[node.i]))
            for k in i_range:
                for n in j_range:
                    if (k != 0 or n != 0) and (abs(k) != 1 or abs(n) != 1):
                        neighbors.append(Point(node.i + k, node.j + n, int(inp[node.i + k][node.j + n])))
            return neighbors

        def dfs(visited, graph, node):
            if f"({node.i},{node.j})" not in visited:
                print(f"Value: {node.value}, i: {node.i}, j: {node.j}")
                visited.add(f"({node.i},{node.j})")
                neighbors = find_neighbors(node)
                for neighbour in neighbors:
                    if neighbour.value != 9:
                        dfs(visited, graph, neighbour)

        dfs(visited, inp, low_point)
        return len(visited)
