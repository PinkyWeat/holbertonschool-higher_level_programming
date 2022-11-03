# Python - Inheritance

---

## Description

### Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent Class** - is the class being inherited from, also called base class.

**Child Class** - is the class that inherits from another class, also called derived class.

### Creating a ``Parent Class``
Any class can be a parent class, so the syntax is the same as creating any other class:

    class Mammal:
        def __init__(self, specie):
            self.__specie = specie

### Creating a ``Child Class``
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

    class Cat(Mammal):
        pass
---

                                            *// under construction site //*

---
### Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all files start with ``#!/usr/bin/python3``
- Code uses the ``pycodestyle`` (version 2.7.x)
- All files will be executables
- Length of files will be tested using ``wc``

---

### Given permits: ``chmod u+x``

---

## File Description

- **0-lookup.py** - file contains function that returns the list of available attributes and methods of an object.
- **1-my_list.py** - file contains a class ``MyList`` that inherits from ``list``.
- **2-is_same_class.py** - file contains a function that returns ``True`` if the object is exactly an instance of the specified class, ``False`` otherwise.
- **3-is_kind_of_class.py** - file contains function that returns ``True`` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise ``False``.
- **4-inherits_from.py** - file contains function that returns ``True`` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ``False``.
- **5-base_geometry.py** - file contains an empty class ``BaseGeometry``.
- **6-base_geometry.py** - file contains a class ``BaseGeometry`` (based on ``5-base_geometry.py``).
- **7-base_geometry.py** - file contains a class ``BaseGeometry`` (based on ``6-base_geometry.py``).
- **8-rectangle.py** - file contains a class ``Rectangle`` that inherits from ``BaseGeometry`` (``7-base_geometry.py``).
- **9-rectangle.py** - file contains a class ``Rectangle`` that inherits from ``BaseGeometry`` (``7-base_geometry.py``) - task based on ``8-rectangle.py``.
- **10-square.py** - file contains a class ``Square`` that inherits from ``Rectangle`` (``9-rectangle.``py``).
- **11-square.py** - file contains a class ``Square`` that inherits from ``Rectangle`` (``9-rectangle.py``). - task based on ``10-square.py``.

**Test Files:**

- **tests/1-my_list.txt**
- **tests/7-base_geometry.txt**

---
### Author

Written by [Denisse Landau](https://www.linkedin.com/in/denisselandau/ "Denisse Landau")