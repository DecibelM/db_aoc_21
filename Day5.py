from collections import Counter
from input import Imports

importClass = Imports()


class Day5:
    @staticmethod
    def task1():
        inp = importClass.getInput("input/input5_test.txt")
        # inp = importClass.getInput("input/input5.txt")

        data = list(map(lambda item: str(item).strip("\n").split("->"), inp))
        for item in data:
            item[0] = item[0].split(",")
            item[1] = item[1].split(",")

        points = []
        points_diag = []

        for item in data:
            # (x1, y1) -> (x2,y2)
            x1 = int(item[0][0])
            x2 = int(item[1][0])
            y1 = int(item[0][1])
            y2 = int(item[1][1])
            if x1 == x2:
                new_points = []
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    new_point = f"({x1},{y})"
                    new_points.append(new_point)
                points.extend(new_points)
            elif y1 == y2:
                new_points = []
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    new_point = f"({x},{y1})"
                    new_points.append(new_point)
                points.extend(new_points)
            elif abs(x1 - x2) == abs(y1 - y2):
                new_points = []
                offset = Day5.get_inclination(x1, x2, y1, y2)
                x = x1
                y = y1
                while x != (x2 + offset[0]):
                    new_point = f"({x},{y})"
                    new_points.append(new_point)
                    x += offset[0]
                    y += offset[1]
                points_diag.extend(new_points)

        counter = Counter(points)
        res = Day5.count_values(counter)
        print(f"Task 1: {res}")

        counter.update(points_diag)
        sum_diag = Day5.count_values(counter)
        print(f"Total sum: {sum_diag}")

    @staticmethod
    def count_values(counter):
        res = 0
        for value in counter.values():
            if value > 1:
                res += 1
        return res

    @staticmethod
    def get_inclination(x1, x2, y1, y2):
        offset = [0, 0]
        offset[0] = 1 if x1 < x2 else -1
        offset[1] = 1 if y1 < y2 else -1
        return offset
