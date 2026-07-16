"""#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)"""
my_list = [5, 7, 9, 11, 2, 3, 5, 12, 7, 2, 11, 15]
unique_list = []
for list in my_list:
    if list not in unique_list:
        unique_list.append(list)
print("original list:", my_list)
print("List without duplicates:", unique_list)


my_numbers = [2, 4, 6, 8, 10, 4, 6, 12, 2] 
my_uniques = []
for list in my_numbers:
    if list not in my_uniques:
        my_uniques.append(list)
print("original list:", my_numbers)
print("List without duplications:", my_uniques)

my_numbers = [2, 4, 6, 8, 10, 4, 6, 12, 2]
print(set(my_numbers))

my_list = [4, 6, 8, 9, 11, 2, 25, 38, 49]
largest = my_list[0]

for number in my_list:
    if number > largest:
        largest = number
print("Largest number:", largest)


my_list = [12, 5, 8, 25, 15, 7]

minimum = my_list[0]

for number in my_list:
    if number < minimum:
        minimum = number

print("minimum number:", minimum)
 
my_list = [12, 5, 8, 25, 15, 7]

largest = my_list[0]
second_largest = my_list[1]

for number in my_list:
    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest:
        second_largest = number

print("Second largest number:", second_largest)


my_list = [1, 3, 5, 7, 2, 3, 7, 9]
numbers = []
for list in my_list:
    if list not in numbers:
        numbers.append(list)
print("original list:", my_list)
print("without duplicates:", numbers)

my_numbers = [10, 20, 30, 40, 50, 60]
my_numbers.pop(5)
my_numbers.pop(4)
my_numbers.pop(0)
print(my_numbers)


my_numbers = [10, 20, 30]
del my_numbers
print(my_numbers)


number_list = [5, 10, 15, 20, 25, 30]
entered_number = int(input("Enter a number: "))
if entered_number in number_list:
    print(f"The number {entered_number} exists in the list.")

    if entered_number % 2 == 0:
        print(f"The number {entered_number} is even.")
    else:
        print(f"The number {entered_number} is odd.")
else:
    print(f"The number {entered_number} is not in the list.")


    for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)

a = 0
b = 1

while a <= 50:
    print(a, end=" ")
    c = a + b
    a = b
    b = c