def my_function(my_int, my_list):
    my_list[2] = 5
    my_int += 4
    print('In function', my_int)
    my_list = [3, 6, 25]
    print('In function', my_list)

my_int = 1
my_list = [0, 1, 2, 3, 4]
my_function(my_int, my_list)
print('my_int', my_int)
print('my_list', my_list)

# a = 5
# b = a
# b += 1
# print('a is', a)
# print('b is', b)
