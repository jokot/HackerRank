import numpy as np

# find max sum of first quadrant of a matrix 2nx2n
def maxSumQuadrant(matrix):
    oneQuarter = matrix[:len(matrix)//2, :len(matrix)//2]
    secondQuarter = np.fliplr(matrix[:len(matrix)//2, len(matrix)//2:])
    thirdQuarter = matrix[len(matrix)//2:, :len(matrix)//2][::-1]
    fourthQuarter = np.flip(matrix[len(matrix)//2:, len(matrix)//2:])
    maxMatrix = []
    for i in range(len(oneQuarter)):
        for j in range(len(oneQuarter[0])):
            maxMatrix.append(max(oneQuarter[i][j], secondQuarter[i][j], thirdQuarter[i][j], fourthQuarter[i][j]))
    return sum(maxMatrix)

if __name__ == '__main__':
    matrix = [[1,2,3,4],
            [5,66,7,8],
            [9,10,11,12],
            [13,14,15,16]]
    # matrix = [[1,2],[3,4]]
    matrix = np.array(matrix)
    print(maxSumQuadrant(matrix))