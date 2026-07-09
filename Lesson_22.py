my_list = [7, 3, 8, 2, 5, 15]
print(my_list)

#Find the maximum value in a list.
maximum = my_list[0]
for item in my_list:
    if item > maximum:
        maximum = item
print("Maximum value:", maximum)

#Find the minimum value in a list.
minimum = my_list[0]
for item in my_list:
    if item < minimum:
        minimum = item
print("minimum value:", minimum)

#Calculate the sum of all elements in a list.
summary = 0
for item in my_list:
    summary += item
print("Sum of all elements:", summary)

#Sort the list in ascending order. Couldn't use built-in sort() or sorted() functions
num = [9, 3, 7, 15]
for i in range(len(num)):
    for j in range(len(num) - 1):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp

print("Sorted list:", num)

