# https://habr.com/post/319164/

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print(my_list)
print(my_dict) # порядок элементов в неиндексированных коллекциях не сохраняется.

print(len(my_list)) # 6
print(len(my_dict)) # 6 - для словаря пара ключ-значение считаются одним элементом. 
print(len('ab c')) # 4 - для строки элементом является 1 символ

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print('a' in my_list)           # True
print('q' in my_list)           # False
print('a' not in my_list)       # False
print('q' not in my_list)       # True

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print('a' in my_dict)               # True - без указания метода поиск по ключам
print('a' in my_dict.keys())        # True - аналогично примеру выше
print('a' in my_dict.values())      # False - так как 'а' — ключ, не значение
print(1 in my_dict.values())        # True
print(('a',1) in my_dict.items())   # True
print(('a',2) in my_dict.items())   # False