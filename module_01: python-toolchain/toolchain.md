# ♻️ **Python Toolchain**

Most of us think that **python is an interpreted language**. While it is true on surface level, but internally it uses a hybrid model:
```
It is compiled first and then interpreted
```
Let us now understand the complete build process of a python code step-by-step. Consider the below short overview of the python build process.
```
Python source code
      |
   Bytecode
      |
     PVM
      |
    Output
```

## 📦 **Bytecode (`.pyc`)**
**A bytecode is a low-level, platform independent intermediate representation of our souce code.** 

When we write a python script (`.py`), the computer's processor cannot understand it directly. Our CPU can only understand raw "machine-code" (`0's` and `1's`). Before our code is executed, python internally compiles our source code. It does not compile it to machine code, instead it translates our python code into intermediate language called as **"bytecodes"**.

>[!NOTE]
>**Bytecodes are neither human-friendly nor in machine code format. It was specifically designed for the python virtual machine (PVM).**

```
Python source code  --->  Python compiler  --->  Bytecode generation  --->  PVM  ->  Output
```
