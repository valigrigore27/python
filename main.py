# # EX1
# class Stack:
#     def __init__(self):
#         self.list = []
#
#     def size(self):
#         return len(self.list)
#
#     def push(self, val):
#         self.list.append(val)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.list.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.list[-1]
#
#     def is_empty(self):
#         return len(self.list) == 0
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# result1 = stack.pop()
# print(result1)
#
# result2 = stack.peek()
# print(result2)
#
# result3 = stack.pop()
# print(result3)
#
# result4 = stack.pop()
# print(result4)
#
# result5 = stack.peek()
# print(result5)
#
# result6 = stack.pop()
# print(result6)
# -------------------------------------------------------------------------------------------
# EX2

# class Queue:
#     def __init__(self):
#         self.list = []
#
#     def size(self):
#         return len(self.list)
#
#     def push(self, val):
#         self.list.append(val)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         val = self.list[0]
#         del self.list[0]
#         return val
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.list[0]
#
#     def is_empty(self):
#         return len(self.list) == 0
#
#
# queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
#
# result1 = stack.pop()
# print(result1)
#
# result2 = stack.peek()
# print(result2)
#
# result3 = stack.pop()
# print(result3)
#
# result4 = stack.pop()
# print(result4)
#
# result5 = stack.peek()
# print(result5)
#
# result6 = stack.pop()
# print(result6)


# -------------------------------------------------------------------------------------------

# class Matrix:
#     def __init__(self, n, m, matrix=None):
#         if matrix is not None:
#             self.matrix = matrix
#         else:
#             self.matrix = self.get_matrix(n, m)
#
#     def __len__(self):
#         return len(self.matrix)
#
#     def __str__(self):
#         return self.get_readable_matrix_string(self.matrix)
#
#     def get_matrix(self, n, m):
#         num = 1
#         matrix = [[None for j in range(m)] for i in range(n)]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 matrix[i][j] = num
#                 num += 1
#         return matrix
#
#     def get_readable_matrix_string(self, matrix):
#         strings = []
#         for row in matrix:
#             strings.append(str(row))
#         return '\n'.join(strings)
#
#     def getElement(self, i, j):
#         return self.matrix[i - 1][j - 1]
#
#     def setElement(self, i, j, element):
#         self.matrix[i][j] = element
#
#     def transpose(self, matrix):
#         return [list(i) for i in zip(*matrix)]
#
#     def getTranspose(self):
#         return self.get_readable_matrix_string(self.transpose(self.matrix))
#
#     def doTranspose(self):
#         self.matrix = self.transpose(self.matrix)
#
#     def multiply(self, other_matrix):
#         if len(self.matrix[0]) != len(other_matrix.matrix):
#             print("Matrix dimensions are not suitable for multiplication")
#
#         result = [[0 for _ in range(len(other_matrix.matrix[0]))] for _ in range(len(self.matrix))]
#
#         for i in range(len(self.matrix)):
#             for j in range(len(other_matrix.matrix[0])):
#                 for k in range(len(other_matrix.matrix)):
#                     result[i][j] += self.getElement(i + 1, k + 1) * other_matrix.getElement(k + 1, j + 1)
#
#         return Matrix(len(self.matrix), len(other_matrix.matrix[0]), result)
#
#     def apply_transform(self, transform_func):
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 self.matrix[i][j] = transform_func(self.matrix[i][j])
#
#
# matrix1 = Matrix(2, 3)
# matrix1.setElement(1, 1, -10)
# print("Matrix1: ")
# print(matrix1)
#
#
# transform = lambda x: x * 2
# matrix1.apply_transform(transform)
# print()
# print(matrix1)
#
#
# print()
# print("Transpose: ")
# print()
# matrix1.doTranspose()
# print(matrix1)
#
#
# print()
# matrix2 = Matrix(2, 3)
# print("Matrix2: ")
# print(matrix2)
#
#
# print()
# print("Multiplication:")
# print()
# mul = matrix1.multiply(matrix2)
# print(mul)
