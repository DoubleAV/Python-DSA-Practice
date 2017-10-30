# Flip matrix along its vertical axis

def flip_vertical_axis(matrix):
    
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

# this is another approach but I like the first a lot better

# def flip_vertical_axis(matrix):
#     r = len(matrix)-1
#     c = len(matrix[0])-1
#     temp = 0
#     i = 0
#     while i <= r:
#         j = 0
#         while j <= c/2:
#             temp = matrix[i][j]
#             matrix [i][j] = matrix[i][c-j]
#             matrix[i][c-j] = temp
#             j += 1
#         i += 1