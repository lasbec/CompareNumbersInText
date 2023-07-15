import pandas as pd
from itertools import zip_longest

    

def filterDigits(str):
    return "".join([c for c in str if c.isdigit()])

def firstDiff(str0, str1):
    result = ""
    for c0, c1 in zip(str0, str1):
        if(c0!=c1):
            return result + " (common prefix)" + "\n  " + c0 + " first difference\n  " + c1 + " first difference"
        result += c0

    return None


class StringSlice:
    def __init__(self, parentString, startIndex, stopIndex):
        self.parentString = parentString
        self.parentLen = len(parentString)
        self.startIndex = startIndex
        self.stopIndex = stopIndex
        self.value = parentString[startIndex:stopIndex]

    def __eq__(self, other):
        if(other == None):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"[{self.startIndex}:{self.stopIndex}]'{self.value}'"

    def __str__(self):
        return self.surroundingSlice().valueWithOpenEndsMarked()

    def valueWithOpenEndsMarked(self):
        leftEndIsOpen = self.startIndex > 0
        rightEndIsOpen = self.stopIndex < self.parentLen
        leftMark = "..." if leftEndIsOpen else ""
        rightMark = "..." if rightEndIsOpen else ""
        return leftMark + self.value + rightMark

    def surroundingSlice(self,radius=10):
        start = self.startIndex - radius
        start = 0 if start < 0 else start

        stop = self.stopIndex + radius
        stop = self.parentLen if stop > self.parentLen else stop

        return StringSlice(self.parentString, start, stop)

class SlicesComparison:
    def __init__(self, slicesLeft, slicesRight):
        self.slicesLeft = slicesLeft
        self.slicesRight = slicesRight
        self.initMisses()
        self.initDifferences()

        
    def initDifferences(self):
        result = []
        for leftDigits, rightDigits in zip_longest(self.slicesLeft, self.slicesRight):
            if(leftDigits != rightDigits):
                result += [(leftDigits, rightDigits)]
        self.differences = result
        self.differencesFound = len(self.differences) > 0
    
    def initMisses(self):
        leftSet = set(self.slicesLeft)
        rightSet = set(self.slicesRight)

        self.leftMisses = rightSet.difference(leftSet)
        self.rightMisses = leftSet.difference(rightSet)




    def __repr__(self):
        if(not self.differencesFound):
            return "No difference found"
        result = ""
        
        (firstDiffLeft, firstDiffRight) = self.differences[0]

        result += "First difference:\n" + str(firstDiffLeft) + "\n" + str(firstDiffRight) + "\n"

        result += "\nLeft misses following elements from right:\n" if len(self.leftMisses) > 0 else ""
        for lm in self.leftMisses:
            result += str(lm) + "\n"
        result += "\nRight misses following elements from left:\n" if (len(self.rightMisses)) > 0 else ""
        for rm in self.rightMisses:
            result += str(rm) + "\n"
        return result


def parseDigitSlices(string):
    result = []
    startOfDigits = None
    for index, char in enumerate(string):
        if (char.isdigit() and startOfDigits == None):
           startOfDigits = index
        elif (not char.isdigit() and startOfDigits != None):
           result.append(StringSlice(string, startOfDigits, index))
           startOfDigits = None
    if(startOfDigits != None): # case last char is a digit   
        result.append(StringSlice(string, startOfDigits, len(string)))
    return result





def main():
    counter = 0
    df = pd.read_excel('Texte.xlsx')
    col1 = df["DE"].tolist()
    col2 = df["FR"].tolist()
    for i,(cell1, cell2) in enumerate(zip(col1, col2)):
        _numbers1 = filterDigits(cell1)
        _numbers2 = filterDigits(cell2)

        numbers1 = parseDigitSlices(cell1)
        numbers2 = parseDigitSlices(cell2)
        
        comp = SlicesComparison(numbers1, numbers2)

        if(comp.differencesFound):
            counter += 1
            print("Differing numbers found in row ",i+2 ,":\n",comp,"--------------------------------------------\n")

        # if numbers1 != numbers2:
        #     counter += 1
        #     print("\nEntry unequal in line", i + 2, "\nRead numbers\n", _numbers1, "\n", _numbers2,"\n", firstDiff(_numbers1, _numbers2)),

    print("Found ", counter, " inconsistencys in total")

main() 