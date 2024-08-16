# CLASSES

"""
- Support multiple inheritance (inheriting from multiple base classes)
- Method overriding
- Methods can call mathods of base class with the same name
- Classes are created at runtime
- Normal class members including data members are public
- All member functions are virtual
- There are no shorthands for referencing the object's members from its methods
- The member functions are declared with an explicit first argument representing
the object, which is provided implicity by the call
- Classes themselves are objects which provides semantics for importing and
renaming
- Built-in types can be used as base classes for extension by the user
- Operator overloading is supported
- Multiple names can be bound to the same object. This is called aliasing. This
can be ignored when dealing with immutable types (numbers, strings, tuples), but
can have effect on mutable objects (lists, dictionaries). Aliases behave as a
pointer, and passing an object becomes cheap when only a pointer is passed by
by the implementation. If a function modifies an object passed as an argument
the caller will see the change
"""

"""
Class Definition Syntax
- Can be placed inside a block (if statement or function definition)
- Statement inside class definitions will mostly be function definitions with
peculiar form of argument list, dictated by the calling convention for methods
- When a class definition is entered, a new namespace is created, and used as
the local scope — thus, all assignments to local variables go into this new
namespace. In particular, function definitions bind the name of the new function
here.
- When a class definition is left normally (via the end), a class object is
created. This is basically a wrapper around the contents of the namespace
created by the class definition. The original local scope (the one in effect
just before the class definition was entered) is reinstated, and the class
object is bound here to the class name given in the class definition header
(ClassName in the example).
"""
class Classname:
    # statement 1
    # statement n
    pass

"""

"""


"""
Private Variables
- Cannot be accessed except from inside an object that doesn't exist in Python
- A name prefixed with _ should be treated as a non-public part of the API. It
should be considered an implementation detail and subject to change
"""


"""
Odds and Evens
- Analogous to C's struct type
- For bundling a few named data items

A piece of Python code that expects a particular abstract data type can often be
passed a class than emulates the methods of that data type instead. If you have
a function that formats some data from a file object, you can define a class
with methods read() and readline() that get the data from a string buffer and
pass it as an argument

Instance method objects have attributes: m.__self__ is the instance object with
the method m() and m.__func__ is the function object corresponding to the method
"""
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee("John", "Computer Lab", 1000)
john.dept       # 'Computer Lab'
john.salary     # 1000

"""
Iterators
- Behind the scenes the for statement calls iter() on the container object
- The function returns an iterator object that defines the method __next__(),
which accesses elements in the container one at a time
- When there are no more elements, __next__() raises a StopIteration exception
which tells the for loop to terminate
- You can call the __next__() method using the next() built-in function
- To add iterator behavior to your classes define an __iter__() method which
returns an object with a __next__() method. If the class defines __next__() then
__iter__() can just return self
"""
s = "abc"
it = iter(s)
it              # <str_iterator object at 0xasdj8024>
next(it)        # 'a'
next(it)        # 'b'
next(it)        # 'c'
next(it)        # StopIteration

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse("spam")
iter(rev)               # <__main__.Reverse object at 0xjd802n>
for char in rev:
    print(char)         # m a p s

"""
Generators
- Used to create iterators
- Written like regular functions but use the yield statement whenever they want
to return data
- next() is called on it, the generator resumes where it left off (it remembers
all the data values and which statement was last executed)
- Anything that can be done with generators can also be done with class-based
iterators. Generators are compact because:
    - __iter__() and __next__() methods are created automatically
    - the local variables and execution state are saved automatically between
    calls, instead of using instance variables like self.data and self.index. 
    - They raise StopIteration() automatically when they terminate
"""
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse("golf"):
    print(char)

"""
Generator Expressions
- Similar to list comprehensions using () instead of []
- Useful in situations where the generator is used right away by an enclosing
function
- They are more memory friendly than list comprehensions
"""
square_sum = sum(i*i for i in range(10))     # sum of squares from 0 to 9

x_vec = [10, 20, 30]
y_vec = [7, 5, 3]
sum(x*y for x, y in zip(x_vec, y_vec))       # dot product

unique_words = set(word for line in page for word in line.split())