value = input("Enter any integer for 1st solution: ")
value = int(value)
new_value_1 = value / 2 if value < 100 else -value
print(f"solution_1: {new_value_1}")

#####################################################

value = 78.23
value = int(value)
new_value_2 = 1 if value < 100 else 0
print(f"solution_2: {new_value_2}")

#####################################################

value = 123
value = int(value)
new_value_3 = True if value < 100 else False
print(f"solution_3: {new_value_3}")

#####################################################

my_str = "Minerva now put it in Penelope’s mind to make the suitors try their skill with the bow and with the iron axes"
my_str = str(my_str)
my_str_4 = my_str.upper()
print(f"solution_4: {my_str_4}")

#####################################################

my_str = "Minerva now put it in Penelope’s mind to make the suitors try their skill with the bow and with the iron axes"
my_str = str(my_str)
my_str_5 = my_str_4.lower()
print(f"solution_5: {my_str_5}")

#####################################################

my_str = "Mine"
my_str = str(my_str)
index = len(my_str)
if index < 5:
    print(f"solution_6: {my_str * 2}")
else:
    print(f"solution_6: {my_str}")

#####################################################

my_str = input("Enter any string for 7th solution: ")
my_str = str(my_str)
index = len(my_str)
if index < 5:
    print(f"solution_7: {my_str [::-1]}")
else:
    print(f"solution_7: {my_str}")

#####################################################

my_str = input("Enter any string for 8th solution: ")
my_str = str(my_str)
for symbol in my_str:
    if symbol in 'eyuioa' or symbol in 'bcdfghjklmnpqrstvwxyz' or symbol in '1234567890':
        print(f"solution_8: {symbol}")

#####################################################

my_str = input("Enter any string for 9th solution: ")
my_str = str(my_str)
my_str_1 = my_str.lower()
for symbol in my_str_1:
    if symbol not in 'eyuioa' and symbol not in 'bcdfghjklmnpqrstvwxyz' and symbol not in '1234567890':
        print(f"solution_9: {symbol}")

#####################################################

my_str = input("Enter any string for 10th solution: ")
my_str = str(my_str)
my_str_1 = my_str.lower()
for symbol in my_str_1:
    if symbol not in 'eyuioa' and symbol not in 'bcdfghjklmnpqrstvwxyz' and symbol not in '1234567890' and symbol != ' ':
        print(f"solution_10: {symbol}")

#####################################################
