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



def do_any():
    print("yo")
class do_some():
    print("hei")

#print(type(do_any))
#a = do_any()
#print(type(a))
#b = do_any()
#print(type(b))



# добавление нового поля к объекту 'function'
def do_some(): 
    try: 
        do_some.a 
    except (AttributeError): 
        do_some.a = 50 
    print(do_some.a) 
    print(type(do_some))
print(type(do_some()))
do_some() 
do_some.a = 30 
do_some()
print("___________")


# принципиально похоже на добавление нового поля к любому объекту
class any_class:
    b = 100
print(type(any_class))
any = any_class()
print(type(any))
any.a = 50
def do_some():
    print(any.a, any.b)
print(type(do_some))
do_some()
any.a = 30
do_some()


# вызов функции == создание объекта класса 'function'?


# проверка отправки в переименованный репозиторий