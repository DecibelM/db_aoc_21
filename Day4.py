from input import Imports

importClass = Imports()

class Day4:
    @staticmethod
    def task1():
        #data = importClass.getInput("input/input4_test.txt")
        data = importClass.getInput("input/input4.txt")
        numbers = data.pop(0).split(',')
        data.pop(0)

        for i in range(0,len(data)):
            data[i] = data[i].split()
        board_start = 0
        next_number = 0
        while len(numbers) > 0:
            next_number = numbers.pop(0)
            board_start = 0
            bingo = False
            if next_number == '93':
                print('93')
                print('93 52 69 29 53')
            for i in range(0, len(data)):
                    if len(data[i]) == 0:
                        board_start = i+1
                    line = data[i]
                    if next_number in data[i]:
                        index = data[i].index(next_number)
                        data[i][index] = 'x'
                        bingo = Day4.check_bingo(data[board_start: board_start + 5], next_number)
                        if bingo:
                            break
            if bingo:
                print("BINGO!")
                print("Bingo at " + str(board_start))
                break
        Day4.print_board(data[board_start: board_start + 5])
        sum = Day4.get_final_sum(data[board_start: board_start + 5])
        print("SUM: " + str(sum))
        print("Number: " + next_number)
        print("Result: " + str(sum * int(next_number)))

    @staticmethod
    def task2():
        #data = importClass.get_input_chunk("input/input4_test.txt")
        data = importClass.get_input_chunk("input/input4.txt")
        numbers = data.pop(0).split(',')

        for i in range(0, len(data)):
            data[i] = data[i].split('\n')
            for j in range(0, len(data[i])):
                data[i][j] = data[i][j].split()

        while len(numbers) > 0:
            next_number = numbers.pop(0)
            bingo = False
            board_index = 0
            while board_index < len(data):
                bingo = False
                current_board = data[board_index]
                if next_number == '82':
                    print('90')
                for line in data[board_index]:
                    if next_number in line:
                        index = line.index(next_number)
                        line[index] = 'x'
                        bingo = Day4.check_bingo(data[board_index], next_number)
                    if bingo and len(data) > 1:
                        data.remove(data[board_index])
                        break
                    elif bingo and len(data) == 1:
                        print("Last board!")
                        Day4.print_board(data[board_index])
                        res = Day4.get_final_sum(data[board_index])
                        print("SUM: " + str(res))
                        print("Number: " + next_number)
                        print("Result: " + str(res * int(next_number)))
                        data.remove(data[board_index])
                        break
                if not bingo:
                    board_index += 1


    @staticmethod
    def get_final_sum(board):
        sum = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] != 'x':
                    sum += int(board[i][j])
        return sum


    @staticmethod
    def check_bingo(board, number):
        print("Checking Bingo...")
        print("Current number: " + number)
        if number == '58':
            print('90')
        for i in range(0, len(board)):
            x_counter = 0
            for j in range(0,len(board[i])):
                if board[i][j] == 'x':
                    x_counter += 1
                if x_counter == len(board):
                    return True

        for j in range(0, len(board)):
            x_counter = 0
            for i in range(0, len(board)):
                if board[i][j] == 'x':
                    x_counter += 1
                if x_counter == len(board):
                    return True
        return False

    @staticmethod
    def print_board(board):
        for line in board:
            print(line)

