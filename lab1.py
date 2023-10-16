# # #EX1
# #functia gcd
# def gcd(a, b):
# 	            if b == 0:
# 		                  return a
# 	            else:
# 		             return gcd(b, a % b)
#
# #citesc n numere
# numbers = list(map(int, input().split()))
# #
#
# x=1
# for j in range(1, len(numbers)):
# 	                            if j==1:
# 		                                x= gcd(numbers[j-1],numbers[j])
# 	                            else:
# 		                             x = gcd(x, numbers[j])
# print (x)

#----------------------------------------------------------------------
#EX 2
#
# def count_vowels(input_string):
#                                  input_string=input_string.lower()
#                                  vowels = {'a', 'e', 'i', 'o', 'u'}
#                                  vowels_count=0
#                                  for char in input_string:
#                                                           if char in vowels:
#                                                                             vowels_count += 1
#                                  return vowels_count
#
# my_input = input()
# count = count_vowels(my_input)
# print(count)



#----------------------------------------------------------------------
#EX3

# def occurrences(string1, string2):
#                                   count = 0
#                                   start = 0
#                                   while True:
#                                              start = string2.find(string1, start)
#                                              if start == -1:
#                                                             break
#                                              count += 1
#                                              start += 1
#                                   return count
#
# string1= input()
# string2=input()
#
# occurrences_count=occurrences(string1, string2)
# print(occurrences_count)


#----------------------------------------------------------------------
#EX4
# def camel_case_to_underscore(input_string):
#     result = []
#     is_first_char = True
#     for char in input_string:
#         if char.isupper():
#             if not is_first_char:
#                 result.append('_')
#             result.append(char.lower())
#         else:
#             result.append(char)
#         is_first_char = False
#
# #transform the list of chars in string
#     final_string = ''.join(result)
#     return final_string
#
# input_string = input()
# underscore_string = camel_case_to_underscore(input_string)
# print(underscore_string)

#----------------------------------------------------------------------
#EX5
#----------------------------------------------------------------------


#EX6
# def reverse_of(num):
#      r_num=0
#      while num!=0:
#          d=num%10
#          r_num=r_num*10+d
#          num=num//10
#      return r_num
#
# def is_palindrome(num):
#     return num == reverse_of(num)
#
# number=int(input())
# if is_palindrome(number):
#     print("It's palindrome")
# else:
#     print("It's not a palindrome")

#----------------------------------------------------------------------
#EX7
# def extract_number(text):
#     num_str = ""
#     found_digit = False
#
#     for char in text:
#         if char.isdigit():
#             num_str += char
#             found_digit = True
#         elif found_digit:
#             break
#
#     if num_str:
#         return int(num_str)
#     else:
#         return None
#
# text = input()
# result = extract_number(text)
#
# if result is not None:
#     print(result)
# else:
#     print("No number found in the text.")

#-----------------------------------------------------------------------

#EX8
# def DecimalToBinary(num):
#         bits=0
#         while num>=1:
#             if(num%2==1):
#                 bits=bits+1
#             num=num//2
#         return bits
#
#
# number = int(input())
# binary_number=DecimalToBinary(number)
# print(binary_number)
#
#
#---------------------------------------------------------------------------
#EX10
# def count_words(text):
#     word_count = text.count(" ") + 1
#     return word_count
#
# # Example usage:
# text = input()
# word_count = count_words(text)
# print(word_count)







