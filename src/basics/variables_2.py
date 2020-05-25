cactus = 3
kind = 'lucky number'
my_str = '{:03} is your {}'.format(cactus, kind)
print(my_str)

cactus = 3
kind = 'lucky number'
my_str = f'{cactus:03} is your {kind}'
print(my_str)


cactus = 4
cactus += 0.5

print(cactus, 'of type', type(cactus))
