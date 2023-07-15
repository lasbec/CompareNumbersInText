import pandas as pd

    

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
        return self.value == other.value

    def __repr__(self):
        return f"[{self.startIndex}:{self.stopIndex}]'{self.value}'"

    def hintString(self):
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

class DigitsComparison:
    def __init__(self, slicesLeft, slicesRight):
        self.slicesLeft = slicesLeft
        self.slicesRight = slicesRight
        
    def differences(self):
        result = []
        for leftDigits, rightDigits in zip(self.sliceLeft, self.sliceRight):
            if(leftDigits != rightDigits):
                result += [(leftDigits, rightDigits)]
        return result


    def __repr__(self):
        return self.differences().__repr__()

        


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
        
        DigitsComparison

        if numbers1 != numbers2:
            counter += 1
            print("\nEntry unequal in line", i + 2, "\nRead numbers\n", _numbers1, "\n", _numbers2,"\n", firstDiff(_numbers1, _numbers2)),

    print("Found ", counter, " inconsistencys in total")

main()