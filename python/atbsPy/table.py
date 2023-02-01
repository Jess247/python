tableData = [['apples', 'cherries', 'oranges', 'banana'], [
    'Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]


def printTable(tData):
    i = 0
    for data in tData:
        print(data[0].ljust(10), data[1].ljust(10),
              data[2].ljust(10), data[3].ljust(10),)


printTable(tableData)
