# Python - Test Driven Development

## Description

The goal for this project personally is to get to know more about the testing of my own coding. ``Doctest`` usage at first is not what I expected for a type of testing to be, turned out to be super interesting and easy to use, pretty straight forward.

The ``doctest`` module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown.

In [this](https://docs.python.org/3.4/library/doctest.html) webpage they state these three main points on common ways to use ``doctest``:

>- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

>- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.

>- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

---

>### Given permits: ``chmod u+x``
>

---
### Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all files start with ``#!/usr/bin/python3``
- Code uses the ``pycodestyle`` (version 2.7.x)
- All files will be executables
- Length of files will be tested using ``wc``

---
### Python Test Cases

- All files are under the ``/tests`` folder
- All tests files are text files - extension ``.txt``
- All test were executed using: ``python3 -m doctest ./tests/*``

---

### File Description

Files containing functions:
>**0-add_integer.py** - contains function that adds 2 integers.
>
>**2-matrix_divided.py** - contains function that divides all elements of a matrix.
>
>**3-say_my_name.py** - contains function that prints My name is ``<first name>`` ``<last name>``
>
> **4-print_square.py** - contains function that prints a square with the character ``#``.
>
> **5-text_indentation.py** - contains function that prints a text with 2 new lines after each of these characters: ``.``, ``?`` and ``:``

Test files with ``doctest``:
>**0-add_integer.txt** - contains doctest corresponding to ``add_integer`` function
>
>**2-matrix_divided.txt** - contains doctest corresponding to ``matrix_divided`` function
>
> **3-say_my_name.txt** - contains ``doctest`` corresponding to ``say_my_name`` function
>
> **3-say_my_name.py** - contains function that prints My name is ``<first name>`` ``<last name>``
>
> **4-print_square.txt** - contains ``doctest`` corresponding to ``print_square`` function
>
> **5-text_indentation.txt** - contains doctest corresponding to ``text_indentation`` function

  *// under construction site //*
---

## Author

Written by [Denisse Landau](https://www.linkedin.com/in/denisselandau/ "Denisse Landau")