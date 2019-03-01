import numpy

grid = numpy.zeros([21, 21])

def rekursi(grid, x = 0, y = 0):
    poss = []
    result = 0

    if x + 1 < len(grid):
        poss.append([x+1, y])

    if y + 1 < len(grid[x]):
        poss.append([x, y+1])

    for i in poss:
        #print('REKUZIONE!')
        result += rekursi(grid, i[0], i[1])

    if poss == []:
        result += 1

    return result

def main():
    for i in range(2, 21):
        print(rekursi(numpy.zeros([i , i])))

main()
