class MyClass:
    def __init__(self):
        self.value = 23
        self.list = [2, 3]


obj = MyClass()
print(type(obj))
print(obj.value)
obj.value = 45
print(obj.value)
print(obj.list)
dictionary = {obj: 1, "ghbvth": 2}
print(dictionary)
print(dictionary[obj])
l = list(dictionary.keys())
print(l[0])
print(obj)
if l[0] is obj:
    print("Один объект")
if l[0] == obj:
    print("Объекты равны")
for key, value in dictionary.items():
    print(type(key), key, value)
obj.value = 67
for key, value in dictionary.items():
    print(type(key), key, value)
# obj = [1, 2, 3]
# print(obj)
print(list(dictionary.keys())[0])
del l[0]
print(l[0])
print(l)
print(list(dictionary.keys())[0])
if list(dictionary.keys())[0] is obj:
    print("Это один объект")
# del obj
# print(obj) # NameError
print(list(dictionary.keys())[0])
print(list(dictionary.keys())[0].value)


# Таким образом значения поля value объекта obj, являющегося ключом в
# словаре dictionary изменилось, а следовательно изменился сам объект ->
#  В качестве ключа словаря могут использоваться как изменяемые,
# так и неизменяемые объекты.
# Но остаётся вопрос: изменяется ли ключ при изменении объекта?
# То есть является ли сам объект (весь) ключом или
# ключом является только его неизменяемая часть?

# print(bytes(list(dictionary.keys())[0]))
# print(bytes(obj))
# if bytes(list(dictionary.keys())[0]) == bytes(obj):
#     print("Значения равны побитово")
# Может быть ключом словаря является строковое представление объекта?
class TheClass:
    def __init__(self):
        self.value = 23
        self.list = [1, 2, 3]

    def __repr__(self):
        return str(self.value) + str(self.list)

    def __str__(self):
        return str(self.list) + str(self.value)


obj = TheClass()
d = {obj: 1, (1, 2): 2}
print(obj)
print(list(d.keys())[0])
if obj is list(d.keys())[0]: print("Оно")
obj.value = 45
obj.list = (1, 2, 3)
if obj is list(d.keys())[0]: print("Он")
print(obj)
print(list(d.keys())[0])
