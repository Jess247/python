tableData = [['apples', 'cherries', 'oranges', 'banana'], [
    'Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]


def printTable(tData):
    colWidth = [0] * len(tData)
    lengthOfList = len(tData[0])

    for tableLen in range(len(tData)):
        # sort list by length
        sortedTable = sorted(tData[tableLen], key=len)
        # set the column width to the largest string (the last)
        colWidth[tableLen] = len(sortedTable[-1])

    for strIndex in range(lengthOfList):
        print()
        for i in range(len(tData)):
            string = tData[i][strIndex]
            print(string.rjust(colWidth[i]), end=' ')


printTable(tableData)
