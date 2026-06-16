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

### **Need for Bytecodes?**
Consider an example,
```python
a = 10
b = 20

print(a + b)
```
The above code is human readble and understandable, but CPU only understands machine instructions. (`1001's`) PVM also does not understand high-level python syntax, so python converts the above code into a simpler instruction set known as "bytecode".

```
This the bytecode instructions for the above code

LOAD_CONST 10
STORE_NAME a

LOAD_CONST 20
STORE_NAME b

LOAD_NAME a
LOAD_NAME b

BINARY_OP +

CALL print
```

>[!NOTE]
> - Bytecode is not a machine code. Machine codes are only executed by the CPU, but bytecodes cannot be executed by the CPU.
> - These are only interpreted and executed by the PVM.

```
Consider analogy,

ENGLISH (python code)      --->      TRANSLATOR (bytecode)      --->      MARATHI (machine code)

Bytecodes are only intermediate language and are platform independent (as it contains only set of instructions).
```

### Common Bytecode Instructions
Following are some common instructions that are executed by the PVM

| Instruction  | Meaning  |
|---|---|
| `LOAD_CONST`  | Load a constant value   |
| `STORE_NAME`  | Store a value in variable  |
| `LOAD_NAME`   | Read a variable  |
| `LOAD_FAST`   | Load local variable  |
| `BINARY_OP`   | Arithmetic operation  |
| `CALL`        | Call a function  |
| `RETURN_VALUE`| Returns the result   |
| `JUMP_FORWARD`| Move execution forward   |

>[!IMPORTANT]
>Python's PVM uses a stack data structure. Memory is always allocated dynamically in python. (it is allocated for whenever the variable is used in action)
