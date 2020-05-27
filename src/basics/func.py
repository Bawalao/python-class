def say_hello():
  print('Hello!')
new_func = say_hello
result = new_func()
print(type(result))
