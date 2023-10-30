# EX1
# def sets(a, b):
#     list = []
#     intersected = []
#     union = []
#
#     for i in a:
#         union.append(i)
#         if i in b:
#             intersected.append(i)
#
#     for j in b:
#         if j not in union:
#             union.append(j)
#
#     a_b = [x for x in a if x not in b]
#
#     b_a = [x for x in b if x not in a]
#     list.append(intersected)
#     list.append(union)
#     list.append(a_b)
#     list.append(b_a)
#
#     return list
#
#
# a = [1, 2, 3, 4]
# b = [2, 3, 5]
# list = sets(a, b)
# print("a: ", a)
# print()
# print("b:", b)
# print()
# print(list)
#

# OR

# def sets(a, b):
#     c = a.union(b)
#     d = a.intersection(b)
#     e = a.difference(b)
#     f = b.difference(a)
#     result = []
#     result.append(c)
#     result.append(d)
#     result.append(e)
#     result.append(f)
#     return result
#
#
# a = {1, 2, 3, 4}
# b = {2, 3, 5}
# result = sets(a, b)
# print("a: ", a)
# print()
# print("b:", b)
# print()
# print(result)

# --------------------------------------------------------------------------------------------------
# EX2
# def dictionary(string):
#     item_counts = {}
#     for item in string:
#         if item in item_counts:
#             item_counts[item] += 1
#         else:
#             item_counts[item] = 1
#     return item_counts
#
#
# string = input()
# item_counts = dictionary(string)
# print(item_counts)
# --------------------------------------------------------------------------------------------------

# EX3
# dict1 = {"name": "John", "age": 30, "location": "USA"}
# dict2 = {"name": "John", "age": 30, "location": "USA"}
#
# for key in dict1.keys():
#     if key in dict2.keys():
#         if dict1[key] != dict2[key]:
#             print("The two dictionaries are not equal")
#             break
#     else:
#         print("The two dictionaries are not equal")
#         break
# else:
#     print("The two dictionaries are equal")
#
# --------------------------------------------------------------------------------------------------
# EX4
# def build_xml_element(tag, content, **kwargs):
#     # open xml
#     xml_element = f"<{tag}"
#
#     for key, value in kwargs.items():
#         xml_element += f' {key}="{value}"'
#
#     # close xml
#     xml_element += f">{content}</{tag}>"
#
#     return xml_element
#
#
# result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
# print(result)

# --------------------------------------------------------------------------------------------------

# EX5
# def validate_dict(rules, dictionary):
#     for key, prefix, middle, suffix in rules:
#         if key in dictionary:
#             value = dictionary[key]
#             if value.startswith(prefix) and middle in value[1:-1] and value.endswith(suffix):
#                 continue
#             else:
#                 return False
#     return True
#
# rules = [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")]
# dictionary = {
#     "key1": "come inside, it's too cold out",
#     "key2": "start of year, middle of the winter",
#     "key3": "not a valid value"
# }
#
# result = validate_dict(rules, dictionary)
# print(result)

# --------------------------------------------------------------------------------------------------

# EX6
# def dictionary(lst):
#     item_counts = {}
#     for item in lst:
#         if item in item_counts:
#             item_counts[item] += 1
#         else:
#             item_counts[item] = 1
#     return item_counts
#
#
# def ex6(lst):
#     unique_count = 0
#     duplicate_count = 0
#     counts = dictionary(lst)
#     for i in counts.values():
#         if i == 1:
#             unique_count += 1
#         elif i == 2:
#             duplicate_count += 1
#
#     return unique_count, duplicate_count
#
#
# words = input().split()
# a, b = ex6(words)
# print(a, b)

# --------------------------------------------------------------------------------------------------
# EX7

# def set_operations(*args):
#     results = {}
#
#     pairs = [(set_a, set_b) for i, set_a in enumerate(args) for j, set_b in enumerate(args) if i < j]
#
#     for set_a, set_b in pairs:
#         key = f"{set_a} | {set_b}"
#         results[key] = set_a | set_b  # Union
#
#         key = f"{set_a} & {set_b}"
#         results[key] = set_a & set_b  # Intersection
#
#         key = f"{set_a} - {set_b}"
#         results[key] = set_a - set_b  # Set difference a-b
#
#         key = f"{set_b} - {set_a}"
#         results[key] = set_b - set_a  # Set difference b-a
#
#     return results
#
# set1 = {1, 2}
# set2 = {2, 3}
#
# result = set_operations(set1, set2)
# for key, value in result.items():
#     print(f"{key}: {value}")


# ------------------------------------------------------------------------------------------------------
# EX8
# def loop(mapping):
#     visited = set()
#     result = []
#     current_key = 'start'
#
#     while current_key not in visited:
#         visited.add(current_key)
#         result.append(mapping[current_key])
#         next_key = mapping.get(current_key)
#         current_key = next_key
#
#     return result
#
#
# mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
# result = loop(mapping)
# print(result)

# ------------------------------------------------------------------------------------------------------

# EX9
# def my_function(*args, **kwargs):
#
#     count = sum(1 for arg in args if arg in kwargs.values())
#     return count
#
#
# result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=4)
# print(result)
