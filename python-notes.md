## CONTROL FLOW

### IF STATEMENT
```python
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
```
- When comparing the same value to several constants use `match` statement

### FOR STATEMENT

- Iterates over the items of any sequence in the ordre that they appear
```python
words = ["cat", "windows", "defenestrate"]
for w in words:
    print(w, len(w))
```

- Iterate over a copy of a collection if you want to modify the original
```python
users = {"Hans": "active", "Elenore": "inactive", "asdf": "active"}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
```

### FUNCTIONS

- Default arguments
```python
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}: # to check if a value exists in sequence
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid User Response")
        print(reminder)

def f(a, L=[]):
    L.append(a)
    return L
def g(a, L=None):
    L.append(a)
    return L
print(f(1), g(1)) # [1], [1]
print(f(2), g(2)) # [1, 2], [2]
print(f(3), g(3)) # [1, 2, 3], [3]
```

- Keyword arguments (Named parameters)
```python
def parrot(voltage, stage="a stiff", action="voom", type="blue"):
    pass
# keyword argument should be after a keyword arguments
parrot(voltage=5.0, "dead")

# *name receives a tuple containing the positional argument beyond the formal parameter
# **name recieves a dictionary containing the keyword arguments beyond the formal parameter
# *name should be before **name
def cheeseshop(kind, *argument, **keywords):
    pass
```

- Special Parameters
```python
def f(pos1, pos2, /, pos_or_key1, pos_or_key2, *, kwd1, kwd2):
    pass

"""
pos1, pos2 - Positional arguments
pos_or_key - Positional or keyword argument
kwd1, kwd2 - Keyword arguments
"""
```

- Arbitrary Argument List - Before the variable number of arguments any number
of normal arguments may occur. They usually will be the last in the list of
formal parameters, because they scoop up all remaining input arguments that are
passed to the function. Any formal parameters after `*args` are keyword-only
argumet
```python
def concat(*args, sep="/"):
    pass


```

### FUNCTION ANNOTATIONS

```python
def f(ham: str, eggs: str = "eggs") -> str:
    print("Arguments: ", ham, eggs)
    return ham + " and " + eggs
```