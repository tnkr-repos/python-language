""

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

"""
10 - BRIEF TOUR OF THE STANDARD LIBRARY

OPERATING SYSTEM INTERFACE
- The os module provides functions for interacting with the operating system
- Always use import os instead of from os import * so that os.open() function
doesn't shadow the built-in open() function

STRING PATTERN MATCHING
- The re module provides regular expression tools for advanced tool processing

MATHEMATICS
- The math module gives access to the underlying C library functions for
floating-point math
- The random module provides tools for making random selections

DATES AND TIMES
- The datetime module supplies classes for manipulating dates and times, and
timezone aware

BATTERIES INCLUDED
- The json and csv packages provide support for their respective filetypes
- The sqlite3 module is a wrapper for the SQLite database library

OUTPUT FORMATTING
- The reprlib module produces a version of repr() customised for abbreviated
displays of large or deeply nested containers
- The pprint module offers control over printing both built-in and user defined
objects in a way that is readable by the interpreter by adding indentation and
line breaks

TOOLS FOR WORKING WITH LISTS
- The array module provides an array object that is like a list that stores only
homogeneous data and stores it more compactly
- The collections module provides a deque object that is like a list with faster
appends and pops from the left side but slower lookups in the middle (for
implementing queues)
- The bisect module provides functions for manipulating sorted lists
- The heapq module provides functions for implementing heaps based on regular
lists. The lowest valued entry is always kept at position zero (min-heap)
"""
import re
re.findall(r"\bf[a-z]*", "which foot or hand fell fastest") # ["foot", "fell", fastest"]

import math
math.cos(math.pi / 4)   # 0.742

import random
random.choice(["apple", "pear", "banana"])
random.sample(range(100), 3)   # [30, 83, 16] - sampling without replacement
random.random()     # 0.1379 - random float
random.randrange(6) # 4 - random integer chosen from range(6)

from datetime import date
now = date.today()
birthday = date(1964, 7, 31)
age = now - birthday    # number of days

import reprlib
reprlib.repr(set("supercalifragilisticexpialidocious")) # "{a, c, d, ...}"

from array import array
a = array("H", [4000, 10, 700, 2222])
sum(a)  # sum of all elements of array a
a[1: 3] # slicing and indexing work as usual

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())  # Handling task1

import bisect
scores = [(100, "perl"), (200, "tcl"), (400, "lua"), (500, "python")]
bisect.insort(scores, (300, "ruby"))
scores  # [(100, "perl"), (200, "tcl"), (300, "ruby"), (400, "lua"), (500, "python")]

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)       # rearrange the list into heap order
heappush(data, -5)  # add a new entry
[heappop(data) for i in range(3)]   # [-5, 0, 1] - fetches the 3 smallest entries

"""
12 - VIRTUAL ENVIRONMENTS AND PACKAGES

- Applications will sometimes need a specific version of a library. It may not
be possible for one Python installation to meet the requirements of every
application. If application A needs version 1.0 of a particular module but
application B needs version 2.0, then the requirements are in conflict and
installing either version 1.0 or 2.0 will leave one application unable to run

- The solution to this problem is to create a virtual environment (a self
contained directory tree that contains a Python installation for a particular
version of Python, plus a number of additional packages). Different applications
can then use different virtual environments, and their dependencies remain
independent of each other's

- To create a virtual environment
python -m venv <environment_name>   # Most common environment name - .venv as
# keeps the directory hidden in the shell and explains why the directory exists

- To activate a virtual environment
source <environment_name>/bin/activate  # Will 

- To deactivate a virtual environment
deactivate

- Package management is done using pip. To install packages
python -m pip install <package_name> # numpy==2.6.0

- To uninstall package
python -m pip uninstall <package_name>  # pandas

- To list all packages installed in the current virtual environment
python -m pip list

- To store all dependencies of an application
python -m pip freeze > requirements.txt

- To install packages from a txt file (to re-create a virtual environment)
python -m pip install -r <file_name>
"""

"""
15 - FLOATING POINT ARITHMETIC

- Most decimal fractions cannot be represented exactly as binary fractions. This
is called Representation Error. As a consequence the decimal floating-point
numbers you enter are only approximated by the binary floating-point numbers
actually stored in the machine (Similar to how 1/3 = 0.3 or 0.33 or 0.333, and
the decimal is always an approximation of the actual fraction, similarly we stop
representing the equivalent binary representation using the first 53 bits
starting with the most significant bit and denominator as a power of 2)

- Python only displays a decimal approximation of the decimal value of the
binary approximation stored by the machine. For heavy floating-point operations
use NumPy package and many other packages
"""

"""
16 - APPENDIX

16.1.2 - EXECUTABLE PYTHON SCRIPTS

- Python scripts can be made directly executable (like shell scripts) by putting
the line
#!/usr/bin/env python3
assuming the interpreter in on the user's PATH at the beginning of the script
and giving the file an executable mode

- The script can be given an executable permission using
chmod +x my_script.py

16.1.3 - THE INTERACTIVE STARTUP FILE

- If you want to have some standard commands executed every time the interpreter
is started set the environment variable PYTHONSTARTUP to the name of a file
containing your startup commands (similar to .profile feature of Unix shells).
You can also change the prompts sys.ps1 and sys.ps2 in this file

- If you want to read an additional startup file from the current directory you
can program this in the global startup using code
if os.path.isfile(".pythonrc.py"):
    exec(open(".pythonrc.py").read())

- If you want to use the startup file in a script you must do this explicitly in
the script:
import os
filename = os.environ.get("PYTHONSTARTUP")
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)
"""