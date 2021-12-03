from input import Imports

importClass = Imports()

class Day3:

    @staticmethod
    def task1():
        data = importClass.getInput("input/input3.txt")
        num_list = [0] * len(data[0])
        for i in range(0, len(data[0])):
            num_list[i] = Day3.count_ones(data, i)

        print(num_list)
        bin_list = Day3.to_most_common(num_list, len(data))
        print(bin_list)
        result = Day3.bin2int1(bin_list)
        print("Result1: " + str(result))

        #Task 2
        data2 = data.copy()
        data3 = data.copy()
        for i in range(0,len(bin_list)):
            most_tmp = []
            no_ones = Day3.count_ones(data2, i)
            most_common = 0
            if no_ones >= len(data2) / 2:
                most_common = 1

            #find most common
            for j in range(0, len(data2)):
                item = data2[j]
                if int(item[i]) == most_common:
                    most_tmp.append(item)
            data2 = most_tmp.copy()
            if len(data2) == 1:
                break

        for i in range(0, len(bin_list)):
            #find least common

            least_common = 0
            no_ones = Day3.count_ones(data3, i)
            if no_ones < len(data3) / 2:
                least_common = 1
            least_tmp = []
            for j in range(0, len(data3)):
                item = data3[j]
                if int(item[i]) == least_common:
                    least_tmp.append(item)
            data3 = least_tmp.copy()
            if len(data3) == 1:
                break

        print(data2)
        print(data3)
        O2 = int(data2[0], 2)
        CO2 = int(data3[0], 2)
        print(str(O2))
        print(str(CO2))
        print("Task2: " + str(O2*CO2))

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
    def bin2int1(list):
        length = len(list)
        sum = 0
        sum2 = 0
        for item in list:
            length -= 1
            sum += item * 2 ** (length)
            sum2 += abs(item-1) * 2 ** (length)
        return sum * sum2

    @staticmethod
    def bin2int(list):
        length = len(list)
        sum_int = 0
        for item in list:
            length -= 1
            sum_int += int(item) * 2 ** length
        return sum_int