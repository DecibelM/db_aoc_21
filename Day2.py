from input import Imports

importClass = Imports()


class Day2:
    @staticmethod
    def task1():
        """
        test_data = "forward 5\n" \
                    "down 5\n" \
                    " forward 8\n" \
                    "up 3\n " \
                    "down 8\n " \
                    "forward 2"
        """
        data = importClass.getInput("input/input2.txt")
        #data = test_data.split("\n")
        hor_pos = 0
        depth = 0
        aim = 0

        for cmd in data:
            cmd_split = cmd.split()
            direction = cmd_split[0]
            number = int(cmd_split[1])
            if direction == "forward":
                hor_pos += number
                depth += aim*number
            elif direction == "up":
                aim -= number
            elif direction == "down":
                aim += number

        print("Task1:" + str(depth*hor_pos))



    @staticmethod
    def task2():
        print(" ")
