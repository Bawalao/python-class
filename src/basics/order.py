from importlib import import_module

restaurant = import_module('noodle_house')
print('From Noodle House, I want', restaurant.order())

restaurant = import_module('panera')
print('From Panera, I want', restaurant.order())
