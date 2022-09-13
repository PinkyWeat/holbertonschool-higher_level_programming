# Python - import & modules
---

## Description

### [What are modules in Python](https://www.programiz.com/python-programming/modules#:~:text=What%20are%20modules%20in%20Python,small%20manageable%20and%20organized%20files.)

    **Modules refer to a file containing Python statements and definitions**

A file containing Python code, for example: ``example.py``, is called a module, and its module name would be ``example``.

We use modules to break down large programs into small manageable and organized files.



### How to import modules in Python?

We can ``import`` the definitions inside a module to another module or the interactive interpreter in Python. . To import our previously defined module example, we type the following in the Python prompt:

    | import example

This does not import the names of the functions defined in ``example`` directly in the current symbol table. It only imports the module name ``example`` there. Using the module name we can access the function using the dot ``.`` operator. For example:

    | example.add(4,5.5)
    | 9.5

---

## File Description

``0-add.py`` - program imports function def ``add(a, b)``: from file ``add_0.py`` & prints result of ``1 + 2 = 3``.

``1-calculation.py`` - program imports functions from file ``calculator_1.py``, does some Maths, and prints result.

``2-args.py`` - program prints the number of and the list of its arguments.

``3-infinite_add.py`` - program prints the result of the addition of all arguments.

``4-hidden_discovery.py`` - program prints all names defined by compiled module ``hidden_4.pyc``.

``5-variable_load.py`` - program imports the variable ``a`` from the file ``variable_load_5.py`` and prints its value.

---

## Author

Written by [Denisse Landau](https://www.linkedin.com/in/denisselandau/ "Denisse Landau")