
class Imports():

    def getInput(self, path):
        f = open (path, "r")
        rules = []
        for x in f:
            rules.append(x.strip())
        return rules