class Imports:
    def getInput(self, path):
        f = open(path, "r")
        rules = []
        for x in f:
            rules.append(x.strip())
        return rules

    def get_input_chunk(self, path):
        f = open(path, "r")
        data = f.read()
        fixed_data = data.split("\n\n")
        return fixed_data

    def getInput_split_by_comma(self, path):
        f = open(path, "r")
        data = f.read()
        fixed_data = data.split(",")
        fixed_data = [int(num) for num in fixed_data]
        return fixed_data
