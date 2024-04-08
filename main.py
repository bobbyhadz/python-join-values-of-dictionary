# Join the Values of a dictionary into a string in Python

my_dict = {'a': 'one', 'b': 'two', 'c': 'three'}


values = ' '.join(my_dict.values())
print(values)  # 👉️ one two three

keys = ' '.join(my_dict)
print(keys)  # 👉️ a b c

items = ' '.join(f'{key} {value}' for key, value in my_dict.items())
print(items)  # 👉️ a one b two c three