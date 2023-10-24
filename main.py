# # EX1
# def fib(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         lst = fib(n - 1)
#         lst.append(lst[-1] + lst[-2])
#         return lst
#
#
# example = int(input())
# number = fib(example)
# print(number)

# --------------------------------------------------------------------------------------------------
# EX2
#
# def prime(list):
#     primes =[]
#     for i in list:
#         c=0
#         for j in range(1,i):
#             if i%j==0:
#                 c+=1
#         if c==1:
#             primes.append(i)
#     print(primes)
# prime([1,55,3,71,24,16])
# --------------------------------------------------------------------------------------------------

# EX3
# def sets(a, b):
#     intersected = []
#     union = []
#
#     for i in a:
#         union.append(i)
#         if i in b:
#                 intersected.append(i)
#
#     for j in b:
#         if j not in union:
#             union.append(j)
#
#     a_b = [x for x in a if x not in b]
#
#     b_a = [x for x in b if x not in a]
#     print("Intersection: ", intersected)
#     print()
#     print("Union: ", union)
#     print()
#     print("a-b: ", a_b)
#     print()
#     print("b-a: ", b_a)
# a=[1, 2, 3, 4]
# b=[2, 3, 5]
# sets(a, b)
# --------------------------------------------------------------------------------------------------

# EX4
# def compose(notes, moves, start_pos):
#     num_notes = len(notes)
#     song = []
#     for move in moves:
#         new_pos = (start_pos + move) % num_notes
#         song.append(notes[new_pos])
#         start_pos = new_pos
#     return song
#
#
# notes = ["do", "re", "mi", "fa", "sol"]
# moves = [1, -3, 4, 2]
# start_pos = 2
#
# res = compose(notes, moves, start_pos)
# print(res)

# --------------------------------------------------------------------------------------------------
# EX5
# def replace(matrix):
#     num_rows = len(matrix)
#     num_cols = len(matrix[0])
#
#     for i in range(num_rows):
#         for j in range(num_cols):
#
#             if i < j:
#                 matrix[i][j] = 0
#
#     return matrix
#
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# res = replace(matrix)
# for row in res:
#     print(row)

# --------------------------------------------------------------------------------------------------

# EX6
# def items_appearing_x_times(x, *lists):
#     item_counts = {}
#
#     for lst in lists:
#         for item in lst:
#             if item in item_counts:
#                 item_counts[item] += 1
#             else:
#                 item_counts[item] = 1
#
#     result = [item for item, count in item_counts.items() if count == x]
#
#     return result
#
#
# list1 = [1, 2, 3]
# list2 = [2, 3, 4, "test"]
# list3 = [4, 5, 6]
# list4 = [4, 1, "test"]
# x = 2
#
# result = items_appearing_x_times(x, list1, list2, list3, list4)
# print(result)

# --------------------------------------------------------------------------------------------------
# EX7
# def reverse_of(num):
#     r_num = 0
#     while num != 0:
#         d = num % 10
#         r_num = r_num * 10 + d
#         num = num // 10
#     return r_num
#
#
# def find_palindrome(list):
#     palindrome_list = []
#     count = 0
#     for i in list:
#         if i == reverse_of(i):
#             count += 1
#             palindrome_list.append(i)
#     greatest_palindrome = max(palindrome_list)
#     return count, greatest_palindrome
#
#
# numbers = [121, 12321, 123, 1221, 45654, 789]
# result = find_palindrome(numbers)
# print("Number of palindromes:", result[0])
# print("Greatest palindrome number:", result[1])

# --------------------------------------------------------------------------------------------------
# EX8
####
####

# --------------------------------------------------------------------------------------------------
# EX9
# def stadium(matrix):
#     result = []
#     for row in range(1, len(matrix)):
#         for col in range(len(matrix[0])):
#             current_element = matrix[row][col]
#             element_above = matrix[row - 1][col]
#             if current_element < element_above:
#                 result.append((row, col))
#     return result
#
#
# matrix =
#     [
#     [1, 2, 3, 2, 1, 1],
#
#     [2, 4, 4, 3, 7, 2],
#
#     [5, 5, 2, 5, 6, 4],
#
#     [6, 6, 7, 6, 7, 5]
#     ]
# result=stadium(matrix)
# print(result)

# --------------------------------------------------------------------------------------------------

# EX11
# def sort_tuples_by_third_character(tuples_list):
#     def custom_sort_key(item):
#         if len(item) >= 2 and len(item[1]) >= 3:
#             return item[1][2]
#         else:
#             return ''
#
#     sorted_list = sorted(tuples_list, key=custom_sort_key)
#     return sorted_list
#
#
# tuples_list = [('apple', 'banana', 'hg'), ('cherry', 'dabe'), ('fig', 'grape')]
# result = sort_tuples_by_third_character(tuples_list)
# print(result)

# --------------------------------------------------------------------------------------------------

# EX12
# def group_by_rhyme(words):
#     rhyme_groups = {}
#
#     for word in words:
#
#         rhyme = word[-2:]
#
#         if rhyme in rhyme_groups:
#             rhyme_groups[rhyme].append(word)
#         else:
#             rhyme_groups[rhyme] = [word]
#
#     grouped_words = list(rhyme_groups.values())
#
#     return grouped_words
#
#
# words = ['ana', 'banana', 'carte', 'arme', 'parte']
# result = group_by_rhyme(words)
# print(result)
