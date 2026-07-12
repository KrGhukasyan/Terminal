"""#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)"""
my_list = [5, 7, 9, 11, 2, 3, 5, 12, 7, 2, 11, 15]
unique_list = []
for list in my_list:
    if list not in unique_list:
        unique_list.append(list)
print("original list:", my_list)
print("List without duplicates:", unique_list)
        