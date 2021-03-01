my_list = [0, 10, 25, 50, 100, 101, 200, 500, 1000]

for value in my_list:
    value = int(value)
    if value > 100:
        print(f'solution 1 = {value}')
print('\n')

########################################################

my_list = [0, 10, 25, 50, 100, 101, 200, 500, 1000]
my_results = []

for value in my_list:
    value = int(value)
    if value > 100:
        my_results.append(value)
print(f'Solution 2 = {my_results}')
print('\n')

########################################################

my_list = [0, 10, 25, 50, 100, 101, 200, 500, 1000]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(f'Solution 3.1 = {my_list}')

########################################################

my_list = [500]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(f'Solution 3.2 = {my_list}')
print('\n')

########################################################

my_list = [0, 10, 25, 50, 100, 101, 200, 500, 1000]
my_indexes = range(len(my_list))  # я намагався створити список індексів, щоб довжина цього списка відповідала my_list
print(f'Solution 5.1 = {my_indexes}')

my_list = [0, 10, 25, 50, 100, 101, 200, 500, 1000]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # не знайшов іншого способа оголосити список індексів, ніж просто перерахувати
for index in my_indexes:
    print(f'Solution 5.2 = {index} - {my_list[index]}')
print('\n')

########################################################

my_list_1 = [1, 3]
my_list_2 = [2, 4]
my_indexes = [0, 1]

print(f'Solution 6 for (1, 3) -> {my_list_1[my_indexes[0]]}, {my_list_2 [my_indexes[0]]}')
print(f'Solution 6 for (2, 4) -> {my_list_1[my_indexes[1]]}, {my_list_2 [my_indexes[1]]}')
print('\n')

########################################################

my_string = '0123456789'
for symb_1 in my_string:
    for symb_2 in my_string:
        print(f'For Solution 7: {symb_1 + symb_2}')
