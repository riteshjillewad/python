# **Dunder (__) Variables**

Dunder variables, a.k.a (double underscore) varaibles are special variables or magic attributes. These are variables whose _**"names start and end with double underscore"**_.

Ex:
```
__name__
__dict__
__class__
__doc__
```

These are created and maintained by python to store metadata about the objects, classes and functions. These are built-in containers that tell us:
* What an object is
* What class it belongs to
* What attributes it contains

>[!IMPORTANT]
>Dunder variables, basically answers the question, **"tu kon ahhe, ani tuza naav kay ahhe ?"**. Since there is not entry point function in python, so every file that we run, runs from the 1st indention. So when we use dunder method, it will tell that this file is internally called as `__main__`.

## **__name__ Variable**
This variable is very important at module level. **It is used to represent the name of module.**

Ex: filename: `test.py`. If we run the following command
```python
print(__name__)            # This will return __main__
```
