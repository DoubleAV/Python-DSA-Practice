#flips 2d matrix along its horizontal axis

def flip_horizontal_axis(matrix):
    size = len(matrix)
    for i in range(size // 2):
        matrix[i], matrix[size - 1 - i] = matrix[size - 1 - i], matrix[i]

#another approach that is nice but kinda shwag for an interview

# def flip_horizontal_axis(matrix):
#     matrix.reverse()

#this approach is harder but probably better for interviews

# def flip_horizontal_axis(matrix):
#     r = len(matrix)-1
#     c = len(matrix[0])-1
#     temp = 0
#     i = 0
#     while i <= r/2:
#         j = 0
#         while j <= c:
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[r-i][j]
#             matrix[r-i][j] = temp
#             j += 1
#         i += 1

testMatrix = [[1,2,3],[4,5,6],[7,8,9]]

flip_horizontal_axis(testMatrix)

print(testMatrix)
