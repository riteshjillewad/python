# Modules

A **module** is a Python file (`.py`) that contains **functions, classes, variables, and executable statements**. Modules are used to organize code into separate files, making programs more structured, reusable, and easier to maintain.

In simple terms, a module is a **collection of related code** stored in a single Python file.

For example, instead of writing all functions in one large file, we can group related functions into different modules such as `math_utils.py`, `string_utils.py`, or `database.py`.

---

## Definition

A **module** is a Python file containing:

- Function definitions
- Class definitions
- Variables (constants or global variables)
- Executable statements

The file must have the **`.py`** extension.

---

## Example

Suppose we create a file named `calculator.py`.

```python
# calculator.py

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

This file itself is called a **module**.

Now another Python program can use it.

```python
import calculator

print(calculator.PI)
print(calculator.add(10, 20))
```

**Output**

```text
3.14159
30
```

---

## Why Do We Need Modules?

Without modules, all the code of a project would be written in a single file, making it:

- Difficult to read
- Difficult to debug
- Difficult to maintain
- Difficult to reuse

Modules solve these problems by dividing the program into smaller, independent files.

---

## Advantages of Modules

- Improve code reusability.
- Reduce code duplication.
- Make programs modular and organized.
- Simplify testing and debugging.
- Improve readability and maintainability.
- Allow multiple developers to work on different parts of the same project.
- Provide a namespace to avoid naming conflicts.

---

## Types of Modules

Python supports three main types of modules:

### 1. Built-in Modules

These modules are already provided by Python.

Examples:

- `math`
- `random`
- `os`
- `sys`
- `time`
- `datetime`

Example:

```python
import math

print(math.sqrt(25))
```

---

### 2. User-Defined Modules

These are modules created by the programmer.

Example:

```text
calculator.py
```

```python
def multiply(a, b):
    return a * b
```

Usage:

```python
import calculator

print(calculator.multiply(5, 6))
```

---

### 3. Third-Party Modules

These modules are developed by external developers and can be installed using `pip`.

Examples:

- `numpy`
- `pandas`
- `matplotlib`
- `requests`
- `flask`

Example:

```python
import pandas as pd
```

---

## Key Points

- A module is simply a Python file (`.py`).
- Modules contain functions, classes, variables, and executable code.
- They help organize large programs into smaller, manageable parts.
- Python provides built-in modules, while programmers can create their own modules or install third-party modules.
- Modules promote code reuse, readability, and maintainability.

---

## Author
Ritesh Jillewad
