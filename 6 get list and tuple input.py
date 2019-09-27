# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

input_list = input("to get list please enter your numbers seperated with comma: ")
list = input_list.split(",")
tuple = tuple(list)
print('List :', list)
print('Tuple:', tuple)