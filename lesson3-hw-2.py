my_str = "String for 8th solution is PK!(#KM) Mm2fmd e2m _Nnd2n9df9udscnon 898 *(yt( "
my_str = str(my_str)
for symbol in my_str:
    if symbol.isalpha() or symbol.isdigit():
        print(f"solution_8: {symbol}")

#####################################################

my_str = input("String for 9th solution: ")
my_str = str(my_str)
my_str_1 = my_str.lower()
for symbol in my_str_1:
    if not symbol.isalpha() or not symbol.isdigit():
        print(f"solution_9: {symbol}")

#####################################################

my_str = "String for 8th solution is PK!(#KM) Mm2fmd e2m _Nnd2n9df9udscnon 898 *(yt( "
my_str = str(my_str)
my_str_1 = my_str.lower()
for symbol in my_str_1:
    if not symbol.isalpha() and not symbol.isdigit() and symbol != ' ':
        print(f"solution_10: {symbol}")
