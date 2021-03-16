# make a list of numbers
# i is used for counting numbers
# add the last two numbers in the list
# print the numbers

list_of_numbers = [1, 1]
i = 2
while i < 13:
    list_of_numbers.append(list_of_numbers[i-2] + list_of_numbers[i-1])
    i += 1
for i in list_of_numbers:
    print(i)
