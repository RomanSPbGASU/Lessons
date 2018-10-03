#arr = [[10, 20, 30], [40, 50, 60]]
#for a, b, c in arr:
#    print(a, b, c)

##import matplotlib
##import numpy
#s = "P\nP"
#print(s)
#s = r"Python\t\nCython"
#print(s)
#print("Кафедра" " математики")
#print(s + " математики")
#print(s[::-1])
#s1 = "%-25s" % s
#print(s1)


## попытка обращения к полю функции извне
#def do_some():
#    if not hasattr(do_some, "a"):
#        a = 50
#    print(a)
#do_some()
#do_some.a = 30
#do_some()   # UnboundLocalError("local variable 'a' referenced before assignment")
#print("__________")


# являются ли переменные, объявленные в теле функции (в области её видимости), полями функции ? (Нет)


#def do_some():
#    a = 50
#    if not 'a' in globals():
#        print("а нет в глобальных")
#    if not 'a' in locals():
#        print("a нет в локальных")
#    if not hasattr(do_some, "a"):
#        print("a нет в атрибутах")
#        a = 50
#    print(a)
#do_some()
#do_some.a = 30
#do_some()
#print("__________")
## Вывод:
##   а нет в глобальных
##   a нет в атрибутах
##   50
##   а нет в глобальных
##   50


# Что делает def ? 



#def do_any():
#    print("yo")
#class do_some():
#    print("hei")

#print(type(do_any))
#a = do_any()
#print(type(a))
#b = do_any()
#print(type(b))



## добавление нового поля к объекту 'function'
#def do_some(): 
#    try: 
#        do_some.a 
#    except (AttributeError): 
#        do_some.a = 50 
#    print(do_some.a) 
#    print(type(do_some))
#print(type(do_some()))
#do_some() 
#do_some.a = 30 
#do_some()
#print("___________")


# принципиально похоже на добавление нового поля к любому объекту
#class any_class:
#    b = 100
#    __dict__["c"] = "abc"
#    if not 'b' in globals():
#        print("b нет в глобальных")
#    if not 'b' in locals():
#        print("b нет в локальных")
#    if not hasattr(do_some, "b"):
#        print("b нет в атрибутах")

#print(type(any_class))
#any = any_class()
#print(type(any))
#any.a = 50
#any.b = 1
#def do_some():
#    print(any.a, any.b)
#print(type(do_some))
#do_some()
#any.a = 30
#do_some()


# вызов функции == создание объекта класса 'function'?



## слияние списков с чередованием
#la = ["a", "b", "c"]
#lb = [1, 2, 3]
## цель получить список ["a", 1, "b", 2, "c", 3]
#res = []
#for i, elem in enumerate(la):
#    l = ([elem] + [lb[i]])
#    l2 = [elem] + [lb[i]]
#    print(l2 == l)
#    print(l2 is l)
#    print(l)
#    for j in l:
#        res.append(j)
#print(res)

#def createGenerator() :
#    mylist = range(3)
#    for i in mylist :
#        yield i*i

#mygenerator = createGenerator()
#print(*mygenerator)


# использование Python для переноса учебных проектов по ООП C++ из разных решений в одно
# part 1. перенос папок проектов в общую папку решения
#import shutil
#import re
#import os
#base_dir = r'D:\Desktop\C++'
#dest_dir = r"D:\Desktop\C++\Lessons Cpp"
#names = os.listdir(base_dir)
#print(os.listdir(dest_dir))
#rex = re.compile(r"^L(1[7-9]|20)\.[0-9].*")
#for dir in names:
#    if rex.search(dir):
#        print(dir)
#        print(base_dir + "\\" + dir)
#        shutil.copytree(base_dir + "\\" + dir, dest_dir + "\\" + dir)
# part 2. добавление проектов в решение
# для этого сгенерируем строку с именами файлов, которую можно вставить в окне Добавление существующего проекта
# добавление с помощью окна добавление нескольких элементов за раз невозможно
# добавить проекты вручную в файл решения не получилось так как там присутствуют дескрипторы/хэш-суммы/т.п.