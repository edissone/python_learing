## Магические методы
Магические методы — это определенные стандартной библиотекой питона методы, которые позволяют выдерживать один и тот же интерфейс для всех классов стандартной библиотеки питона. Правило названия — `__name__`.

Пример: 
```python
# создаем список и строку
array = [1, 2, 3]
string = "123"

# почему мы узнаем длину строки и списка одним методом? 
len(array) == len(string)
# это работает так, потому что функция len определена как-то так
def len(obj):
    return obj.__len__()

# Соответственно классы списка и имплементируют метод __len__()
# Значит, в своих классах мы тоже можем пользоваться этим
# Например, если бы мы делали класс очереди и хотели бы, чтобы можно было
# узнавать ее длину через len(), то мы бы сделали вот так

class Queue:

    def __init__(self):
        self.entries = []
    
    def __len__(self):
        return len(self.entries)

queue = Queue()
queue.entries = [1, 2, 3]

assert len(queue) == 3
``` 
 
Выше было базовое определение магических методов и способ их применения. В общем, правило такого, что если наш класс имплементирует 
какое-то поведение, аналогия которому есть в стандартном питоне, то мы имплементируем его через магические методы.

Полный список магических методов можно найти в стандартной [доке](https://docs.python.org/3/reference/datamodel.html?highlight=__#special-method-names).

Доп ссылки:
- https://www.tutorialsteacher.com/python/magic-methods-in-python
- https://rszalski.github.io/magicmethods/
- http://zetcode.com/python/magicmethods/

## Итераторы и генераторы
https://docs.python.org/3/glossary.html#term-iterable

### Iterators
An iterator is an object that implements the iterator protocol. An iterator protocol is nothing but a specific class in Python which further has the `__next__()` method. Which means every time you ask for the next value, an iterator knows how to compute it. It keeps information about the current state of the iterable it is working on. The iterator calls the next value when you call `next()` on it. An object that uses the `__next__()` method is ultimately an iterator. Iterators help to produce cleaner looking code because they allows us to work with infinite sequences without having to reallocate resources for every possible sequence, thus also saving resource space. 

An iterable is any object, not necessarily a data structure that can return an iterator. Its main purpose is to return all of its elements. Iterables can represent finite as well as infinite source of data. An iterable will directly or indirectly define two methods: the `__iter__()` method, which must return the iterator object and the `__next__()` method with the help of the iterator it calls.

### Generators
The generator allows you to write iterators in a much easier syntax where you do not have to write classes with `__iter__()` and `__next__()` methods.
`yield` basically replaces the return statement of a function but rather provides a result to its caller without destroying local variables. Thus, in the next iteration, it can work on this local variable value again. So unlike a normal function, where on each call it starts with new set of variables - a generator will resume the execution where it was left off.

Generators can be of two different types in Python: generator functions and generator expressions.

A generator function is a function where the keyword yield appears in the body. Which means the appearance of the keyword yield is enough to make the function a generator function.
The generator expressions are the generator equivalent of a list comprehension. They can be specially useful for a limited use case. Just like a list comprehension returns a list, a generator expressions will return a generator.

Доп ссылки:
- Iterators vs Generators https://nvie.com/posts/iterators-vs-generators/
- itertools https://docs.python.org/3/library/itertools.html#module-itertools
