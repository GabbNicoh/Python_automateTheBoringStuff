def printTable(table):
    for column in range(len(table[0])): 
        for row in range(len(table)):
            print(table[row][column].rjust(7), end='')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)