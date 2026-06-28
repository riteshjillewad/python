# ♻️ Python Toolchain

Most people think that **Python is an interpreted language**. While this is true at a high level, **CPython (the reference implementation of Python)** follows a **hybrid execution model**:

```text
Python source code → Compiled into Bytecode → Executed by the Python Virtual Machine (PVM)
```

Rather than compiling directly into machine code like C or C++, Python first compiles the source code into an intermediate representation called **bytecode**. The **Python Virtual Machine (PVM)** then interprets this bytecode and performs the corresponding operations, ultimately causing the CPU to execute the required machine instructions.

---

## Overall Execution Flow

```text
Python Source Code (.py)
          │
          ▼
 Lexical Analysis (Tokenizer)
          │
          ▼
        Parser
          │
          ▼
 Abstract Syntax Tree (AST)
          │
          ▼
 Python Compiler
          │
          ▼
 Bytecode (.pyc)
          │
          ▼
 Python Virtual Machine (PVM)
          │
          ▼
 Machine Instructions Executed by CPU
          │
          ▼
        Output
```

> [!IMPORTANT]
> Python does **not** generate native machine code directly. Instead, it compiles the source code into **bytecode**, which is executed by the **Python Virtual Machine (PVM)**.

---

# 📦 Bytecode (`.pyc`)

**Bytecode** is a **low-level, platform-independent intermediate representation** of Python source code.

When we write a Python program (`.py`), the CPU cannot execute it directly because it understands only machine instructions (binary instructions).

Before execution, Python **compiles** the source code into **bytecode**.

```text
Python Source Code
        │
        ▼
Python Compiler
        │
        ▼
Bytecode (.pyc)
        │
        ▼
Python Virtual Machine (PVM)
        │
        ▼
Output
```

> [!NOTE]
> Bytecode is **not human-readable** and **not machine code**. It is a compact instruction set designed specifically for the **Python Virtual Machine (PVM)**.

---

## Why Do We Need Bytecode?

Consider the following program:

```python
a = 10
b = 20

print(a + b)
```

This code is easy for humans to understand, but the CPU cannot execute Python syntax directly.

Therefore, Python first converts it into bytecode instructions.

Example (simplified):

```text
LOAD_CONST      10
STORE_NAME      a

LOAD_CONST      20
STORE_NAME      b

LOAD_NAME       a
LOAD_NAME       b

BINARY_OP       +

CALL            print
RETURN_VALUE
```

These instructions are then interpreted by the **Python Virtual Machine**.

---

## Important Points

> [!IMPORTANT]
>
> - Bytecode is **not machine code**.
> - Bytecode is **platform independent**.
> - The CPU cannot execute bytecode directly.
> - The **Python Virtual Machine (PVM)** reads each bytecode instruction, interprets it, and performs the corresponding operation.
> - During execution, the CPU ultimately executes the machine instructions generated as the PVM performs these operations.

---

## A Simple Analogy

Think of the execution process like this:

```text
Python Source Code
        │
        ▼
English Notes
        │
        ▼
Interpreter (PVM)
        │
        ▼
Machine Instructions
        │
        ▼
CPU
```

Here,

- Python source code is the high-level language.
- Bytecode is an intermediate instruction set.
- The PVM interprets the bytecode.
- The CPU executes the resulting machine instructions.

---

### Common Bytecode Instructions

| Instruction | Description |
|-------------|-------------|
| `LOAD_CONST` | Load a constant value |
| `STORE_NAME` | Store a value in a variable |
| `LOAD_NAME` | Read a variable |
| `LOAD_FAST` | Load a local variable |
| `BINARY_OP` | Perform an arithmetic operation |
| `CALL` | Call a function |
| `RETURN_VALUE` | Return a value |
| `JUMP_FORWARD` | Move execution forward |

---

> [!IMPORTANT]
> The **Python Virtual Machine (PVM)** is **stack-based**, meaning most bytecode instructions operate on an internal stack.
>
> Python also uses **dynamic memory allocation**, where memory for objects is allocated automatically at runtime by Python's memory manager.

---

## Where Are Bytecodes Stored?

Python stores compiled bytecode in **`.pyc`** files.

Example:

```text
program.py
        │
        ▼
program.cpython-315.pyc
        │
        ▼
__pycache__/
```

Example project:

```text
Project/
│
├── main.py
│
└── __pycache__/
      └── main.cpython-315.pyc
```

> [!IMPORTANT]
> `.pyc` files are **cached compiled bytecode**.
>
> If the source file has not changed, Python can reuse the cached bytecode instead of recompiling the source code, reducing startup time.

> [!NOTE]
> `.pyc` files are generally created for imported modules. Depending on how a program is executed, the main script may not always produce a cached `.pyc` file.

---

## How to View Bytecode?

Python provides the built-in **`dis` (disassembler)** module.

The `dis` module converts bytecode into a human-readable form.

Example:

```python
import dis

dis.dis("a = 10")
```

Example output (Python version may vary):

```text
  0 RESUME                   0
  2 LOAD_CONST               0 (10)
  4 STORE_NAME               0 (a)
  6 LOAD_CONST               1 (None)
  8 RETURN_VALUE
```

---

## Summary

- Python follows a **compile-then-interpret** execution model.
- Source code (`.py`) is compiled into **bytecode (`.pyc`)**.
- Bytecode is **platform independent**.
- Bytecode is executed by the **Python Virtual Machine (PVM)**.
- The PVM interprets bytecode and performs operations that ultimately execute as machine instructions on the CPU.
- Cached bytecode is stored inside the `__pycache__` directory to improve startup performance.
- The `dis` module allows developers to inspect generated bytecode.

---

# 🖥️ Python Virtual Machine (PVM)

The **Python Virtual Machine (PVM)** is the runtime engine of Python that **executes Python bytecode**. It acts as an intermediary between the compiled bytecode and the computer's hardware.

After the Python compiler converts the source code (`.py`) into **bytecode (`.pyc`)**, the PVM reads and executes the bytecode instruction by instruction.

Unlike the CPU, which executes machine code directly, the PVM understands **Python bytecode** and performs the required operations to produce the final output.

The PVM is a software component and is part of the Python interpreter (CPython).

---

## Execution Flow

```text
Python Source Code (.py)
            │
            ▼
    Python Compiler
            │
            ▼
    Bytecode (.pyc)
            │
            ▼
 Python Virtual Machine (PVM)
            │
            ▼
 Executes Bytecode Instructions
            │
            ▼
 Machine Instructions Executed by CPU
            │
            ▼
          Output
```

> [!IMPORTANT]
> The **PVM does not execute Python source code directly**. It executes the **bytecode** generated by the Python compiler.

---

## Why Do We Need the PVM?

The CPU can execute only **machine code**, whereas Python programs are written in a **high-level language**.

The PVM bridges this gap by interpreting Python bytecode and performing the corresponding operations.

Without the PVM, Python programs could not be executed.

---

## How Does the PVM Work?

Suppose we have the following Python program:

```python
a = 10
b = 20

print(a + b)
```

### Step 1

The Python compiler converts the source code into bytecode.

```text
LOAD_CONST 10
STORE_NAME a

LOAD_CONST 20
STORE_NAME b

LOAD_NAME a
LOAD_NAME b

BINARY_OP +

CALL print
RETURN_VALUE
```

### Step 2

The PVM reads one instruction at a time.

For example,

```text
LOAD_CONST 10
```

The PVM pushes the value `10` onto its internal stack.

```text
STORE_NAME a
```

The value is stored in the variable `a`.

Similarly, every instruction is interpreted and executed until the program finishes.

---

## Stack-Based Execution

The Python Virtual Machine uses a **stack-based architecture**.

Instead of storing intermediate values in registers, it uses an internal **evaluation stack**.

Example

```python
print(10 + 20)
```

Simplified execution

```text
LOAD_CONST 10

Stack
-------
10

LOAD_CONST 20

Stack
-------
20
10

BINARY_OP +

Stack
-------
30

CALL print

Output
30
```

Every arithmetic operation is performed using values stored on this stack.

> [!NOTE]
> This internal stack is managed automatically by the PVM and is not directly accessible to the programmer.

---

## Architecture of the Python Virtual Machine (PVM)

The following diagram illustrates the high-level architecture of the PVM.

```text
                Python Program (.py)
                         │
                         ▼
                 Python Compiler
                         │
                         ▼
                  Bytecode (.pyc)
                         │
                         ▼
             Python Virtual Machine (PVM)
         ┌────────────────────────────────┐
         │                                │
         │  Bytecode Interpreter          │
         │                                │
         │  Evaluation Stack              │
         │                                │
         │  Memory Manager                │
         │                                │
         │  Object Manager                │
         │                                │
         │  Garbage Collector             │
         │                                │
         └────────────────────────────────┘
                         │
                         ▼
               Operating System
                         │
                         ▼
                        CPU
                         │
                         ▼
                       Output
```

---

## Components of the PVM

### 1. Bytecode Interpreter

- Reads bytecode instructions.
- Executes one instruction at a time.
- Controls the execution flow of the program.

---

### 2. Evaluation Stack

Stores temporary values during execution.

For example,

```python
10 + 20 * 5
```

The operands are pushed onto the stack, operations are performed, and the results are pushed back onto the stack.

---

### 3. Memory Manager

Responsible for:

- Creating Python objects
- Allocating memory
- Releasing unused memory

Python automatically manages memory; programmers do not manually allocate or free memory.

---

### 4. Object Manager

Every value in Python is an object.

The Object Manager handles:

- Object creation
- Object references
- Object metadata
- Type information

---

### 5. Garbage Collector

Automatically removes objects that are no longer referenced.

This helps prevent memory leaks and reduces manual memory management.

---

## Facts About the PVM

### 1. The PVM is Software

The PVM is **not hardware**.

It is a software component included with the Python interpreter.

---

### 2. It Executes Bytecode

The PVM **does not execute Python source code**.

It executes **Python bytecode**.

---

### 3. It is Platform Dependent

Although Python bytecode is platform independent, the **PVM implementation is platform dependent** because it interacts with the operating system and hardware.

Each operating system has its own Python interpreter executable.

Examples:

- Windows → `python.exe`
- Linux → `python`
- macOS → `python3`

---

### 4. Bytecode is Platform Independent

The same bytecode can be executed on different operating systems, provided an appropriate Python interpreter is available.

---

### 5. The PVM Uses a Stack

Unlike many CPUs that are register-based, the PVM performs most operations using an internal **evaluation stack**.

---

### 6. Every Python Object Lives in Memory

Numbers, strings, lists, dictionaries, functions, and even classes are objects managed by the PVM.

---

### 7. Memory Allocation is Automatic

Python performs **dynamic memory allocation**.

Memory is allocated automatically when objects are created.

---

### 8. Garbage Collection is Automatic

Unused objects are removed automatically by Python's garbage collector.

Programmers do not need to explicitly free memory.

---

### 9. The PVM is Part of CPython

In the standard Python implementation (**CPython**), the PVM is built into the interpreter.

Other Python implementations have their own virtual machines.

Examples:

| Python Implementation | Virtual Machine |
|-----------------------|-----------------|
| CPython | Python Virtual Machine (PVM) |
| PyPy | PyPy Virtual Machine with JIT Compiler |
| Jython | Java Virtual Machine (JVM) |
| IronPython | .NET Common Language Runtime (CLR) |

---

### 10. The PVM is Responsible for Program Execution

The PVM controls:

- Function calls
- Loops
- Exception handling
- Memory management
- Object creation
- Arithmetic operations
- Module loading

Almost every Python statement is ultimately executed by the PVM.

---

## Summary

- The **Python Virtual Machine (PVM)** is the runtime engine of Python.
- It executes **Python bytecode**, not Python source code.
- It uses a **stack-based architecture** for execution.
- It automatically manages memory and objects.
- It includes components such as the Bytecode Interpreter, Evaluation Stack, Memory Manager, Object Manager, and Garbage Collector.
- It is responsible for executing Python programs and interacting with the operating system and CPU.


# 🚀 Python Build Process (Execution Pipeline)

The **Python Build Process**, also known as the **Execution Pipeline**, is the sequence of steps that Python follows to execute a program.

Unlike languages such as C or C++, Python does **not** compile the source code directly into machine code. Instead, it first compiles the source code into **bytecode**, which is then executed by the **Python Virtual Machine (PVM)**.

The complete execution process is automatic and is handled internally by the Python interpreter.

---

## Overview

```text
Python Source Code (.py)
          │
          ▼
  Lexical Analysis
          │
          ▼
        Parsing
          │
          ▼
 Abstract Syntax Tree (AST)
          │
          ▼
  Bytecode Compilation
          │
          ▼
 Bytecode (.pyc)
          │
          ▼
Python Virtual Machine (PVM)
          │
          ▼
Operating System
          │
          ▼
CPU Executes Machine Instructions
          │
          ▼
        Output
```

> [!IMPORTANT]
> Python follows a **compile-then-interpret** execution model. The source code is first compiled into **bytecode**, and the bytecode is then interpreted by the **Python Virtual Machine (PVM)**.

---

## Step 1: Writing the Source Code

The process begins when the programmer writes a Python program and saves it with the **`.py`** extension.

Example

```python
a = 10
b = 20

print(a + b)
```

This file is called the **source code**.

---

## Step 2: Lexical Analysis (Tokenization)

The first internal step is **Lexical Analysis**.

The Python interpreter reads the source code character by character and breaks it into small meaningful units called **tokens**.

These tokens are the basic building blocks of the Python language.

For the statement

```python
a = 10
```

the generated tokens are:

```text
NAME        a
OP          =
NUMBER      10
NEWLINE
```

Some common types of tokens include:

- Keywords
- Identifiers
- Operators
- Literals
- Delimiters

---

## Step 3: Parsing

After tokenization, Python checks whether the sequence of tokens follows the grammar rules of the language.

This process is called **Parsing**.

If the syntax is correct, Python proceeds to the next step.

Otherwise, a **SyntaxError** is raised.

Example

```python
if x > 10
    print(x)
```

Output

```text
SyntaxError: expected ':'
```

---

## Step 4: Abstract Syntax Tree (AST) Generation

If parsing is successful, Python creates an **Abstract Syntax Tree (AST)**.

An AST is a tree-like representation of the program's logical structure.

It does **not** contain every character of the source code. Instead, it represents the relationships between statements and expressions.

Example

```python
x = 5 + 10
```

Simplified AST

```text
Assignment
├── Variable (x)
└── Binary Operation (+)
      ├── 5
      └── 10
```

The AST is easier for the compiler to analyze and optimize.

---

## Step 5: Bytecode Compilation

The AST is passed to the **Python Compiler**.

The compiler converts the AST into **bytecode**.

Bytecode is a low-level, platform-independent instruction set understood by the **Python Virtual Machine (PVM)**.

Example (simplified)

```text
LOAD_CONST      5
LOAD_CONST      10
BINARY_OP       +
STORE_NAME      x
```

> [!NOTE]
> Bytecode is **not machine code**. It is an intermediate representation specifically designed for the Python Virtual Machine.

---

## Step 6: Storing Bytecode

Python may store the compiled bytecode as a **`.pyc`** file inside the `__pycache__` directory.

Example

```text
Project/
│
├── main.py
│
└── __pycache__/
      └── main.cpython-315.pyc
```

These files act as **cached bytecode**.

If the source file has not changed, Python can reuse the cached bytecode instead of recompiling it, improving program startup time.

> [!NOTE]
> Cached `.pyc` files are commonly created for imported modules. The main script executed directly may not always generate a cached bytecode file.

---

## Step 7: Python Virtual Machine (PVM)

The compiled bytecode is then loaded into the **Python Virtual Machine (PVM)**.

The PVM reads the bytecode **one instruction at a time** and executes it.

Example

```text
LOAD_CONST
STORE_NAME
LOAD_NAME
CALL
RETURN_VALUE
```

The PVM uses an internal **evaluation stack** to perform operations such as arithmetic calculations, function calls, and object manipulation.

---

## Step 8: Interaction with the Operating System

Whenever a program needs services such as:

- Reading a file
- Printing output
- Creating a process
- Allocating memory
- Accessing the network

the PVM communicates with the **Operating System**.

The operating system provides these services and returns the results to the PVM.

---

## Step 9: CPU Executes Machine Instructions

The CPU cannot execute Python source code or bytecode directly.

As the PVM interprets each bytecode instruction, it performs the required operations, which ultimately result in machine instructions being executed by the CPU.

The CPU processes these instructions and completes the requested operations.

---

## Step 10: Output Generation

Finally, the results are displayed to the user.

Example

```python
print(10 + 20)
```

Output

```text
30
```

At this stage, the entire execution pipeline has completed successfully.

---

## Complete Execution Pipeline

```text
Programmer
     │
     ▼
Writes Python Source Code (.py)
     │
     ▼
Lexical Analysis (Tokenizer)
     │
     ▼
Parser
     │
     ▼
Abstract Syntax Tree (AST)
     │
     ▼
Python Compiler
     │
     ▼
Bytecode (.pyc)
     │
     ▼
Python Virtual Machine (PVM)
     │
     ▼
Operating System
     │
     ▼
CPU
     │
     ▼
Output
```

---

## Key Points

- Python follows a **compile-then-interpret** execution model.
- Source code is first converted into **tokens** during lexical analysis.
- The parser checks the syntax of the program.
- A valid program is transformed into an **Abstract Syntax Tree (AST)**.
- The Python compiler converts the AST into **bytecode**.
- Bytecode is stored as **`.pyc`** files for caching when appropriate.
- The **Python Virtual Machine (PVM)** executes the bytecode instruction by instruction.
- The PVM communicates with the operating system whenever system-level services are required.
- The CPU ultimately executes the machine instructions generated through the PVM's execution.
- This entire process is automatic and transparent to the programmer.

---

## Summary Table

| Step | Description |
|------|-------------|
| 1 | Write Python source code (`.py`) |
| 2 | Perform Lexical Analysis (Tokenization) |
| 3 | Parse the tokens and validate syntax |
| 4 | Generate the Abstract Syntax Tree (AST) |
| 5 | Compile the AST into Bytecode |
| 6 | Store cached bytecode (`.pyc`) when appropriate |
| 7 | Execute bytecode using the Python Virtual Machine (PVM) |
| 8 | Interact with the Operating System for system services |
| 9 | CPU executes the resulting machine instructions |
| 10 | Display the program output |

---
## Author
Ritesh Jillewad
