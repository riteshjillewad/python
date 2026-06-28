# Dunder (`__`) Variables

Dunder variables (short for **double underscore variables**) are special variables, also known as **magic attributes**, provided by Python.

Their names always **start and end with double underscores (`__`)**.

## Examples

```python
__name__
__dict__
__class__
__doc__
```

These variables are automatically created and maintained by the Python interpreter to store **metadata** about modules, objects, classes, and functions.

They provide information such as:

- What an object is
- Which class it belongs to
- What attributes it contains
- How Python internally identifies it

> [!IMPORTANT]
> Think of dunder variables as answering the questions:
>
> **"Who are you, and what is your name?"**
>
> In Marathi:
>
> **"तु कोण आहेस, आणि तुझं नाव काय आहे?"**
>
> Since Python does not have a dedicated entry point function like `main()` in C or Java, execution begins from the first executable statement of the file.
>
> Python internally assigns the special variable `__name__` to identify whether the file is being executed directly or imported as a module.

---

## `__name__` Variable

The `__name__` variable is one of the most important dunder variables.

It represents the **name of the current module**.

### Example

Suppose the filename is:

```text
test.py
```

```python
print(__name__)
```

### Output

```text
__main__
```

---

## When a Python File is Executed Directly

Before executing any Python file, the interpreter automatically initializes several special variables.

One of these is:

```python
__name__
```

If the file is **executed directly**, Python assigns:

```python
__name__ = "__main__"
```

### Example

```python
print("Always executed")

if __name__ == "__main__":
    print("Executed only when the file is run directly")
else:
    print("Executed when imported")
```

### Output

```text
Always executed
Executed only when the file is run directly
```

Since the file is executed directly, its `__name__` becomes `__main__`.

---

## When the File is Imported

Suppose we have a file named:

```text
script.py
```

```python
print(__name__)
```

Now create another file:

```python
import script
```

In this case, Python **does not** assign `__main__` to the imported file.

Instead:

```python
__name__ = "script"
```

Therefore, the following block will **not execute**:

```python
if __name__ == "__main__":
    print("Executed only when run directly")
```

because

```python
__name__ == "script"
```

---

## Need for `if __name__ == "__main__"`

At first, this statement may seem unnecessary.

However, it solves an important problem.

Suppose you have a file containing useful functions.

### calculator.py

```python
def add(a, b):
    return a + b

print("Calculator module loaded")
```

Now another file imports it.

### main.py

```python
import calculator

print(calculator.add(10, 20))
```

### Output

```text
Calculator module loaded
30
```

The message

```text
Calculator module loaded
```

was printed even though we only wanted to use the `add()` function.

This happens because **Python executes every top-level statement while importing a module.**

---

## Solution

Place testing or demonstration code inside the following block:

```python
if __name__ == "__main__":
    # Testing code
```

### calculator.py

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

### main.py

```python
import calculator

print(calculator.add(5, 7))
```

### Output

```text
12
```

Notice that the testing code inside `calculator.py` was **not executed** during import.

---

## Why is This Useful?

Using

```python
if __name__ == "__main__":
```

allows the same Python file to serve two purposes:

- As an executable program
- As an importable module

This keeps the module clean and prevents unwanted code from running during imports.

---

## Summary

| Situation | Value of `__name__` |
|-----------|---------------------|
| File executed directly | `__main__` |
| File imported as a module | Module name |

---

## Key Points

- `__name__` is a special (dunder) variable.
- It stores the name of the current module.
- When a file is run directly, `__name__` is set to `__main__`.
- When imported, `__name__` becomes the module's filename.
- The statement `if __name__ == "__main__":` ensures that certain code runs **only when the file is executed directly**.
- It is commonly used for testing, demonstrations, and defining the entry point of a Python program.

## Author
Ritesh Jillewad
