from input import Imports

importClass = Imports()


class Day3:
    @staticmethod
    def task1():
        data = importClass.getInput("input/input3.txt")
        num_list = [0] * len(data[0])
        for i in range(0, len(data[0])):
            num_list[i] = Day3.count_ones(data, i)

        bin_list = Day3.to_most_common(num_list, len(data))
        result = Day3.bin2int(bin_list)
        print("Result1: " + str(result))

        # Task 2
        data2 = data.copy()
        data3 = data.copy()
        for i in range(0, len(bin_list)):
            no_ones = Day3.count_ones(data2, i)
            most_common = 0
            if no_ones >= len(data2) / 2:
                most_common = 1

            # find oxygen rate
            filtered_iterator = filter(
                lambda item: str(item)[i] == str(most_common), data2
            )
            data2 = list(filtered_iterator)
            if len(data2) == 1:
                break

        for i in range(0, len(bin_list)):
            # find CO2 scrubber rate
            least_common = 0
            no_ones = Day3.count_ones(data3, i)
            if no_ones < len(data3) / 2:
                least_common = 1
            filtered_iterator = filter(
                lambda item: str(item)[i] == str(least_common), data3
            )
            data3 = list(filtered_iterator)
            if len(data3) == 1:
                break

        O2 = int(data2[0], 2)
        CO2 = int(data3[0], 2)
        print("Task2: " + str(O2 * CO2))

    @staticmethod
    def to_most_common(list, length):
        bin_list = [0] * len(list)
        for item in range(0, len(list)):
            if list[item] > length / 2:
                bin_list[item] = 1
            else:
                bin_list[item] = 0
        return bin_list

    @staticmethod
    def count_ones(data, i):
        counter = 0
        for no in data:
            counter += int(no[i])
        return counter

    @staticmethod
    def bin2int(list):
        length = len(list)
        sum = 0
        sum2 = 0
        for item in list:
            length -= 1
            sum += item * 2 ** (length)
            sum2 += abs(item - 1) * 2 ** (length)
        return sum * sum2
