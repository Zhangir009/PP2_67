# Practice3 —  Simple Python Examples

This project contains **simple Python examples** designed for beginners (school level).
It covers **four main topics**:

1. Functions  
2. Lambda expressions  
3. Classes  
4. Inheritance  

Each file can be run independently and prints results using `print()`.

---

## Project Structure

```
Practice3/
├── functions/
│   ├── basic_functions.py
│   ├── function_arguments.py
│   ├── return_values.py
│   └── args_kwargs.py
├── lambda/
│   ├── lambda_basics.py
│   ├── lambda_with_map.py
│   ├── lambda_with_filter.py
│   └── lambda_with_sorted.py
├── classes/
│   ├── class_definition.py
│   ├── init_method.py
│   ├── class_methods.py
│   └── class_variables.py
├── inheritance/
│   ├── inheritance_basics.py
│   ├── super_function.py
│   ├── method_overriding.py
│   └── multiple_inheritance.py
└── README.md
```

---

## How to Run the Code

Open a terminal (CMD / PowerShell / Terminal) and navigate to the folder that contains `Practice3`.

Example:
```bash
cd path/to/your/folder
```

Run any file like this:
```bash
python Practice3/functions/basic_functions.py
python Practice3/lambda/lambda_basics.py
python Practice3/classes/class_definition.py
python Practice3/inheritance/inheritance_basics.py
```

If `python` does not work, try:
```bash
python3 Practice3/functions/basic_functions.py
```

---

## What Each Folder Contains

### 1) Functions (`functions/`)
**Goal:** Learn how to create and use functions.

- `basic_functions.py`  
  Very basic functions (add numbers, check even/odd, greeting).

- `function_arguments.py`  
  Function arguments: default values, `*args`, `**kwargs`.

- `return_values.py`  
  Returning values from functions (single value and multiple values).

- `args_kwargs.py`  
  Simple usage of `*args` and `**kwargs`.

---

### 2) Lambda (`lambda/`)
**Goal:** Learn short anonymous functions (lambda).

- `lambda_basics.py`  
  Basic lambda examples.

- `lambda_with_map.py`  
  Using `lambda` with `map()` to transform data.

- `lambda_with_filter.py`  
  Using `lambda` with `filter()` to select data.

- `lambda_with_sorted.py`  
  Using `lambda` with `sorted()` for custom sorting.

---

### 3) Classes (`classes/`)
**Goal:** Learn object-oriented programming basics.

- `class_definition.py`  
  Simple `Person` class.

- `init_method.py`  
  `__init__` method and simple object methods.

- `class_methods.py`  
  Instance methods, `@classmethod`, and `@staticmethod`.

- `class_variables.py`  
  Difference between class variables and instance variables.

---

### 4) Inheritance (`inheritance/`)
**Goal:** Learn how classes inherit from other classes.

- `inheritance_basics.py`  
  Basic inheritance (`Animal -> Dog`).

- `super_function.py`  
  Using `super()` to call parent class methods.

- `method_overriding.py`  
  Method overriding (same method name, different behavior).

- `multiple_inheritance.py`  
  Multiple inheritance and method resolution order (MRO).

---

## Common Beginner Mistakes

- `IndentationError` - incorrect spacing (tabs/spaces).
- `NameError` - variable or function name is incorrect.
- `TypeError` - wrong number or type of arguments.
- Python not found - Python is not installed or not added to PATH.

---

## Tip for Learning

- Modify the code and see what changes.
- Add `print()` statements to understand what happens step by step.
- Run files one by one and read the output.
