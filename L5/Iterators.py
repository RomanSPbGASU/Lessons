import abc
import collections
from abc import ABCMeta
from collections.abc import Iterable
from string import ascii_letters


class Aggregate(abc.ABC):
    @abc.abstractmethod
    def iterator(self):
        """ Возвращает итератор"""
        ...


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        pass

    @abc.abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Вызывает ошибку StopIteration, если достигнут конец последовательности.
        """
        pass

    @abc.abstractmethod
    def current(self):
        """ Возвращает текущий элемент"""
        pass


class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: индекс с которого начнётся перебор коллекции.
        так же должна быть проверка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Начальное значение курсора -1.
        Так как в нашей реализации сначала
        необходимо вызвать next, который сдвинет курсор на 1
        """
        self._cursor = -1

    def next(self):
        """
        Если курсор указывавет на последний элемент, то вызывает
        StopIteration, иначе сдвигаем курсор на 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """ Возвращаем текущий элемент"""
        return self._collection[self._cursor]


class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


class Iterable(metaclass=ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            from collections import _check_methods
            return _check_methods(C, "__iter__")
        return NotImplemented


class SomeIterable1(collections.abc.Iterable):
    def __iter__(self):
        pass


class SomeIterable2(collections.abc.Iterable):
    def __iter__(self):
        pass


class SomeIterable3:
    def __getitem__(self, key):
        return ascii_letters[key]


class Iterator(Iterable):
    __slots__ = ()

    @abc.abstractmethod
    def __next__(self):
        """Return the next item from the iterator. When exhausted, raise
        StopIteration"""

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            from collections import _check_methods
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented


class ListIterator(collections.abc.Iterator):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        return self._collection[self._cursor]


class ListCollection(collections.abc.Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection, -1)


if __name__ == "__main__":
    # collection = (1, 2, 5, 6, 8)
    # aggregate = ListCollection(collection)
    # itr = aggregate.iterator()
    #
    # while True:
    #     try:
    #         itr.next()
    #     except StopIteration:
    #         break
    #     print(itr.current())
    #
    # itr.first()
    #
    # while True:
    #     try:
    #         itr.next()
    #     except StopIteration:
    #         break
    #     print(itr.current())
    # print(isinstance(SomeIterable1(), collections.abc.Iterable))
    # print(isinstance(SomeIterable2(), collections.abc.Iterable))
    # for item in SomeIterable3():
    #     print(item)
    collection = [1, 2, 5, 6, 8]
    aggregate = ListCollection(collection)

    for item in aggregate:
        print(item)

    print("*" * 50)

    itr = iter(aggregate)
    while True:
        try:
            print(next(itr))
        except StopIteration:
            break
