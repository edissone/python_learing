1. The built-in enumerate function allows us to get not just the elements of a sequence, but also the index of each element, as in:
```python
for index, letter in enumerate('abc'):
    print(f"{index}: {letter}")
```
Create your own MyEnumerate class, such that someone can use it instead of enumerate. It will need to return a tuple with each iteration, with the first element in the tuple being the index (starting with 0), and the second element being the current element from the underlying data structure. Trying to use MyEnumerate with a non-iterable argument will result in an error.

2. Define a class, Circle, which takes two arguments when defined — a sequence and a number. The idea is that the object will then return elements the defined number of times. If the number is greater than the number of elements, then the sequence repeats as necessary.
```python
c = Circle('abc', 5)
print(list(c))        # prints a, b, c, a, b
```
You should define two classes - one to hold data and another to iterate through it.
```python
class CircleIterator:
    ...
class Circle:
    ...
```