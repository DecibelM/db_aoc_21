from input import Imports
from collections import Counter

importClass = Imports()


class Path:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to


class Node:
    def __init__(self, position, is_multiple):
        self.position = position
        self.is_multiple = is_multiple


def print_nodes(inp):
    for row in inp:
        [print(f"{item.position}") for item in row]
        print("------------------------------")


def print_path(inp):
    [print(f"{row.fr},{row.to}") for row in inp]
    print("------------------------------")


def isVisited(visited, current):
    visited_counter = Counter(visited)
    most_common = visited_counter.most_common(1)
    if current == "start" and "start" in visited:
        return True
    elif len(visited) > 0 and current in visited and most_common[0][1] > 1:
        return True
    else:
        return False


class Day12:
    @staticmethod
    def task1():
        # inp = importClass.getInput("input/input12_test.txt")
        inp = importClass.getInput("input/input12.txt")
        inp = list(map(lambda row: row.split("-"), inp))
        inp_paths = list(map(lambda row: Path(row[0], row[1]), inp))

        result = Day12.search(inp_paths, "start")

        print_nodes(result)
        print(len(result))

    @staticmethod
    def search(inp_paths, start):
        visited = []
        start_node = Node(start, start.isupper())
        nodes = {start_node.position: start_node}

        neighbor_dict = {}
        for path in inp_paths:
            if path.fr not in neighbor_dict:
                neighbor_dict[path.fr] = [Node(path.to, path.to.isupper())]
            else:
                neighbor_dict[path.fr].append(Node(path.to, path.to.isupper()))

            if path.to not in neighbor_dict:
                neighbor_dict[path.to] = [Node(path.fr, path.fr.isupper())]
            else:
                neighbor_dict[path.to].append(Node(path.fr, path.fr.isupper()))

        def dfs(visited, graph, node):

            if not isVisited(visited, node.position):
                print(f"Node: {node.position}")
                if not node.is_multiple:
                    visited.append(node.position)
                neighbors = neighbor_dict[node.position]
                paths = []
                path = [node]
                for neighbour in neighbors:
                    if neighbour.position != "end":
                        new_path = dfs(list(visited), graph, neighbour)
                        if new_path is not None and len(new_path) > 0:
                            for p in new_path:
                                partial_path = path + p
                                paths.append(partial_path)
                    else:
                        path.append(Node("end", False))
                        paths.append(path)
                return paths

        paths = dfs(visited, inp_paths, start_node)
        return paths
