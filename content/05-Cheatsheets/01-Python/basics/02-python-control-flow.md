# Python Cheatsheets, vol.2: Introduction to Control Flow

Python provides a versatile set of tools for programming beginners. Mastering the basics, including comments, variables, math operators, and functions, sets the foundation for more advanced coding concepts. Keep exploring, practicing, and building to enhance your Python skills!

As the second part of our **Introduction**, we'll focus on the following learning path for our cheatsheets:

**Control Flow**:
- Conditional statements (if, else, elif).
- Loops (for, while).

Let'sss go!

<p align="center">
  <img src="../../images/snake-hss.png" alt="A hss snake coming out of a box.">
</p>

---

## Table of Contents

1. [🔍 Comparison Operators](#1--comparison-operators)
2. [🔐 Boolean Operators](#2--boolean-operators)
3. [🔄 Mixing Operators](#3--mixing-operators)
4. [🤔 if Statements](#4--if-statements)
5. [❓ Ternary Conditional Operator](#5--ternary-conditional-operator)
6. [🔄📦 Switch-Case Statement](#6--switch-case-statement)
7. [🔄🔄 while Loop Statements](#7--while-loop-statements)
8. [⛔ break Statements](#8--break-statements)
9. [✅ continue Statements](#9--continue-statements)
10. [🔄 For loop](#10--for-loop)
11. [🔢 The range() function](#11--the-range-function)
12. [🔁🤔 For else statement](#12--for-else-statement)
13. [⛔🏁 Ending a Program with sys.exit()](#13--ending-a-program-with-sysexit)
14. [🏛 License](#-license)

---

## 1. 🔍 Comparison Operators

Comparison operators evaluate to True or False depending on the values you give them.

### Examples:

```python
>>> 7 == 7
True

>>> 7 == 8
False

>>> 'apple' == 'apple'
True

>>> 'apple' == 'orange'
False

>>> 'cat' != 'dog'
True

>>> 7 == 7.0
True

>>> 7 == '7'
False
```

---

## 2. 🔐 Boolean Operators

Boolean operators (`and`, `or`, and `not`) are used to combine conditional statements.

### Truth Tables:

**and Operator:**

| Expression        | Evaluates to |
| ----------------- | ------------ |
| `True and True`   | `True`       |
| `True and False`  | `False`      |
| `False and True`  | `False`      |
| `False and False` | `False`      |

**or Operator:**

| Expression       | Evaluates to |
| ---------------- | ------------ |
| `True or True`   | `True`       |
| `True or False`  | `True`       |
| `False or True`  | `True`       |
| `False or False` | `False`      |

**not Operator:**

| Expression  | Evaluates to |
| ----------- | ------------ |
| `not True`  | `False`      |
| `not False` | `True`       |

---

## 3. 🔄 Mixing Operators

You can mix boolean and comparison operators for complex conditions.

### Examples:

```python
>>> (4 < 5) and (5 < 6)
True

>>> (4 < 5) and (9 < 6)
False

>>> (1 == 2) or (2 == 2)
True

>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True

>>> 5 > 4 or 3 < 4 and 5 > 5
True

>>> (5 > 4 or 3 < 4) and 5 > 5
False
```

---

## 4. 🤔 if Statements

The `if` statement evaluates an expression and executes the following indented code if the expression is `True`.

### Examples:

```python
>>> name = 'Debora'

>>> if name == 'Debora':
...    print('Hi, Debora')
...
# Hi, Debora

>>> if name != 'George':
...    print('You are not George')
...
# You are not George
```

**else Statement:**

```python
>>> name = 'Debora'

>>> if name == 'George':
...    print('Hi, George.')
... else:
...    print('You are not George')
...
# You are not George
```

**elif Statement:**

```python
>>> name = 'George'

>>> if name == 'Debora':
...    print('Hi Debora!')
... elif name == 'George':
...    print('Hi George!')
...
# Hi George!
```

---

## 5. ❓ Ternary Conditional Operator

The ternary operator offers one-line code to evaluate expressions based on a condition.

### Example:

```python
>>> age = 15

>>> print('kid' if age < 18 else 'adult')
# Output: kid
```

---

## 6. 🔄📦 Switch-Case Statement

Switch-Case statements were introduced in Python 3.10 for structural pattern matching.

### Matching single values:

```python
>>> response_code = 201
>>> match response_code:
...     case 200:
...         print("OK")
...     case 201:
...         print("Created")
...     # ... other cases ...
...
# Created
```

### Matching with the or Pattern:

```python
>>> response_code = 502
>>> match response_code:
...     case 200 | 201:
...         print("OK")
...     # ... other cases ...
...
# Internal Server Error
```

### Matching by the length of an Iterable:

```python
>>> today_responses = [200, 300, 404, 500]
>>> match today_responses:
...     case [a]:
...         print(f"One response today: {a}")
...     case [a, b]:
...         print(f"Two responses today: {a} and {b}")
...     case [a, b, *rest]:
...         print(f"All responses: {a}, {b}, {rest}")
...
# All responses: 200, 300, [404, 500]
```

### Default value:

```python
>>> response_code = 800
>>> match response_code:
...     case 200 | 201:
...         print("OK")
...     # ... other cases ...
...     case _:
...         print("Invalid Code")
...
# Invalid Code
```

### Matching Builtin Classes:

```python
>>> response_code = "300"
>>> match response_code:
...     case int():
...         print('Code is a number')
...     case str():
...         print('Code is a string')
...     case _:
...         print('Code is neither a string nor a number')
...
# Code is a string
```

### Guarding Match-Case Statements:

```python
>>> response_code = 300
>>> match response_code:
...     case int():
...         if 99 < response_code < 500:
...             print('Code is a valid number')
...     case _:
...         print('Code is an invalid number')
...
# Code is a valid number
```

---

## 7. 🔄🔄 while Loop Statements

The `while` statement is used for repeated execution as long as an expression is `True`.

### Example:

```python
>>> count = 0
>>> while count < 5:
...     print('Hello, world.')
...     count += 1
...
# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.
#

 Hello, world.
```

---

## 8. ⛔ break Statements

If the execution reaches a `break` statement, it immediately exits the `while` loop’s clause.

### Example:

```python
>>> while True:
...     name = input('Please type your name: ')
...     if name == 'your name':
...         break
...
>>> print('Thank you!')
# Please type your name: your name
# Thank you!
```

---

## 9. ✅ continue Statements

When the program execution reaches a `continue` statement, it jumps back to the start of the loop.

### Example:

```python
>>> while True:
...     name = input('Who are you? ')
...     if name != 'Joe':
...         continue
...     password = input('Password? (It is a fish.): ')
...     if password == 'swordfish':
...         break
...
>>> print('Access granted.')
# Who are you? Charles
# Who are you? Debora
# Who are you? Joe
# Password? (It is a fish.): swordfish
# Access granted.
```

---

## 10. 🔄 For loop

The `for` loop iterates over a sequence (e.g., list, tuple, dictionary, set, or string).

### Example:

```python
>>> fruits = ['Apple', 'Banana', 'Cherry']
>>> for fruit in fruits:
...     print(fruit)
...
# Apple
# Banana
# Cherry
```

---

## 11. 🔢 The range() function

The `range()` function generates a sequence of numbers.

### Example:

```python
>>> for i in range(5):
...     print(f'Iteration: {i}')
...
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4
```

### Custom range:

```python
>>> for i in range(0, 10, 2):
...    print(i)
...
# 0
# 2
# 4
# 6
# 8
```

---

## 12. 🔁🤔 For else statement

The `for-else` statement specifies a statement to execute if the full loop has been executed.

### Example:

```python
>>> for i in [1, 2, 3, 4, 5]:
...    if i == 3:
...        break
... else:
...    print("Executed when no item is equal to 3")
```

---

## 13. ⛔🏁 Ending a Program with sys.exit()

The `sys.exit()` function allows exiting Python.

### Example:

```python
>>> import sys

>>> while True:
...     feedback = input('Type exit to exit: ')
...     if feedback == 'exit':
...         print(f'You typed {feedback}.')
...         sys.exit()
...
# Type exit to exit: open
# Type exit to exit: close
# Type exit to exit: exit
# You typed exit
```


**[⬆ Back to Index](#table-of-contents)**

**[🔙 Back to Main Index](../../README.md)**

---

## 🏛 License

Although I am the owner of the examples provided (always taking into account previous examples that I used during my formation, of course. I won't reinvent the wheel today, guys!), I would want to send -again!- some ssssuper-huge-thanks to [Olivia Redanz](https://drawception.com/player/542622/olivia-redanz/) for her fantastic illustration! As for the rest, remember that you can make the Dinosaur extremely happy if you...
<br />

---

<h1 align="center">
  <a href="https://karamazfolio.xyz/"><img src="/images/karaMagister.png" width="200" height="200" alt="Original KaraMagister logo asset.">
</h1>
<h2 align="center">
  <a href="https://www.buymeacoffee.com/JuditKaramazov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 207px !important;" ></a>
</h2> 
