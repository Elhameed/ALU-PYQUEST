#!/usr/bin/python3

PROBLEM_SETS = [
    {
        "question": "What is the output of the following code?\n\n class Animal:\n\t def init(self, name):\n\t\t self.name = name\n\n class Dog(Animal):\n\t\t def bark(self):\n\t\t\t person1 = Person("John", 25)\n\t\t\t print(person1.name)\n",
        "options": {
            "a": "age 25",
            "b": "john 25",
            "c": "John",
            "d": "None of the above"
        },
        "answer": "d"
    },
    {
        "question": "What is the output of the following code?\n\n class Animal:\n\t def __init__(self, name):\n\t self.name = name\n\n class Dog(Animal):\n\tdef bark(self):\n\tprint('Woof!')\n\nmy_dog = Dog('Fido')\nprint(my_dog.name)\nmy_dog.bark()\n",
        "options": {
            "a": "Woof",
            "b": "error",
            "c": "Fido",
            "d": "Woof! Fido"
        },
        "answer": "d"
    },
    {
        "question": "What's the output of the following Python code?\n\ndef add_numbers(x, y):\n\t return x + y\n\nresult = add_numbers(5, 7)\nprint(result)",
        "options": {
            "a": "10",
            "b": "11",
            "c": "12",
            "d": "13"
        },
        "answer": "c"
    },
    {
        "question": "How do I use functions in Python?",
        "options": {
            "a": "By using the def keyword to define a function and calling the function by passing arguments",
            "b": "By using the for loop to define a function and calling the function by passing arguments",
            "c": "By using the if-else statement to define a function and calling the function by passing arguments",
            "d": "None of the above"
        },
        "answer": "a"
    },
    {
        "question": "How can I deal with modules in Python?",
        "options": {
            "a": "Using import statement",
            "b": "Using from...import statement",
            "c": "Using as statement",
            "d": "All of the above"
        },
        "answer": "d"
    },
    {
        "question": "What is the output of the following code?\n\ndef greet(name):\n\tprint('Hello, ' + name + '!')\n\nimport mymodule\n\nmymodule.greet('Alice')\n",
        "options": {
            "a": "Hello, mymodule!",
            "b": "Hello, Alice!",
            "c": "Hello, World!",
            "d": "An error occurs"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = 10\nx, y = y, x\nprint(x, y)",
        "options": {
            "a": "5 10",
            "b": "10 5",
            "c": "Error",
            "d": "None of the above"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[::2])",
        "options": {
            "a": "[1, 3, 5]",
            "b": "[2, 4]",
            "c": "[1, 2, 3, 4, 5]",
            "d": "[1, 4]"
        },
        "answer": "a"
    },
    {
        "question": "Which of the following is NOT a valid numeric type in Python?",
        "options": {
            "a": "int",
            "b": "float",
            "c": "double",
            "d": "complex"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n\nfor i in range(2, 10, 2):\n    print(i)",
        "options": {
            "a": "2 4 6 8",
            "b": "2 4 8",
            "c": "2 6",
            "d": "4 8"
        },
        "answer": "a"
    },
    {
        "question": "What is the value of x after the following code executes?\n\nx = 'Python'\nx += ' is great!'\n",
        "options": {
            "a": "'Python is great!'",
            "b": "'Pythonis great!'",
            "c": "'Python isgreat!'",
            "d": "'Python is great'"
        },
        "answer": "a"
    }
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "options": {
            "a": "Lists are immutable while tuples are mutable",
            "b": "Tuples are immutable while lists are mutable",
            "c": "Lists and tuples are both immutable",
            "d": "Lists and tuples are both mutable"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following is NOT a valid way to create an empty list in Python?",
        "options": {
            "a": "my_list = []",
            "b": "my_list = list()",
            "c": "my_list = list([])",
            "d": "my_list = ()"
        },
        "answer": "d"
    },
    {
        "question": "What is the output of the following code?\n\nimport math\nprint(math.pi)",
        "options": {
            "a": "3.14",
            "b": "3.14159265359",
            "c": "22/7",
            "d": "Undefined"
        },
        "answer": "b"
    },
    {
        "question": "Which keyword is used in Python to handle exceptions?",
        "options": {
            "a": "throw",
            "b": "except",
            "c": "catch",
            "d": "try"
        },
        "answer": "d"
    },
    {
        "question": "Which of the following is an example of inheritance in Python?",
        "options": {
            "a": "class Car:\n def init(self):\n self.color = 'red'\n\nclass SportsCar(Car):\n def init(self):\n super().init()\n self.top_speed = 200",
            "b": "class Animal:\n def init(self):\n self.name = 'Animal'\n def make_sound(self):\n print('generic animal sound')\n\nclass Dog(Animal):\n def make_sound(self):\n print('bark')",
            "c": "class Rectangle:\n def init(self, width, height):\n self.width = width\n self.height = height\n\nclass Square(Rectangle):\n def init(self, side_length):\n super().init(side_length, side_length)",
            "d": "class Person:\n def init(self, name):\n self.name = name\n\nperson1 = Person('Alice')\nperson2 = Person('Bob')"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\nclass MyClass:\n def init(self):\n self.my_var = 42\n\nmy_obj = MyClass()\nprint(my_obj.my_var)",
        "options": {
            "a": "MyClass",
            "b": "my_obj",
            "c": "42",
            "d": "Undefined"
        },
        "answer": "c"
    }
    {
        "question": "What is the purpose of the __init__ method in a Python class?",
        "options": {
            "a": "To create an instance of the class.",
            "b": "To define the class hierarchy.",
            "c": "To define class methods.",
            "d": "To initialize the attributes of an object created from the class."
        },
        "answer": "d"
    },
    {
        "question": "What is the output of the following code?\n\nmy_list = [1, 2, 3, 4]\nprint(my_list[2:])",
        "options": {
            "a": "[1, 2]",
            "b": "[3, 4]",
            "c": "[2, 3, 4]",
            "d": "[1, 2, 3]"
        },
        "answer": "b"
    },
    {
        "question": "What is the purpose of the super() function in Python?",
        "options": {
            "a": "To call the parent class method from within a subclass method.",
            "b": "To create a new instance of a class.",
            "c": "To access the attributes of a superclass.",
            "d": "To define a new class."
        },
        "answer": "a"
    },
    {
        "question": "Which of the following is NOT a valid way to import a module in Python?",
        "options": {
            "a": "import my_module",
            "b": "from my_module import my_function",
            "c": "import my_module.my_function",
            "d": "from my_module import *"
        },
        "answer": "c"
    },
    {
        "question": "Which one of the following data structures in python in immutable?",
        "options": {
            "a": "Tuple",
            "b": "Set",
            "c": "Dictionary",
            "d": "List"
        "question": "Which of these definitions correctly describes a module?",
        "options": {
            "a": "Any program that reuses code",
            "b": "Defines the specification of how it is to be used",
            "c": "Denoted by triple quotes for providing the specification of certain program elements",
            "d": "Design and implementation of specific functionality to be incorporated into a program"
        },
        "answer": "d"
    },
    {
        "question": "To include the use of functions which are present in the random library, we must use the option:",
        "options": {
            "a": "random.h",
            "b": "import.random",
            "c": "import random",
            "d": "random.random"
        },
        "answer": "c"
    },
    {
        "question": "The output of the following Python code is either 1 or 2.\nimport random\nrandom.randint(1,2)",
        "options": {
            "a": "True",
            "b": "False"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code set([1, 2, 3, 2, 1])?",
        "options": {
            "a": "set([1, 2, 3])",
            "b": "set[1, 2, 3, 2, 1]",
            "c": "{1, 2, 3, 2, 1}",
            "d": "{1, 2, 3}"
        "question": "What do these lines print?\na = [5, 7, 9, 11]\na[-1]",
        "options": {
            "a": "-1",
            "b": "[11, 9, 7, 5]",
            "c": "11",
            "d": "7"
        },
        "answer": "c"
    },
    {
        "question": "What do these lines print?\nfor i in range(5, 8):\n    print(i, end=\" \")",
        "options": {
            "a": "5 6 7 8",
            "b": "5 6 7",
            "c": "0 5 6 7",
            "d": "5,6,7"
        },
        "answer": "b"
    },
    {
        "question": "What does this python program output?\ndef dem(name, age):\n    print(name, age)\ndem(\"Ben\", 25)",
        "options": {
            "a": "25",
            "b": "Ben",
            "c": "Ben 25",
            "d": "error"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following is correct?",
        "options": {
            "a": "defunct(a, b)",
            "b": "def add(a, b):",
            "c": "define add(a + b):",
            "d": "define add(a + b)"
        },
        "answer": "b"
    },
    {
        "question": "What do these lines print?\na = { 'id': 89, 'name': \"John\" }\na.get('age', 0)",
        "options": {
            "a": "'age'",
            "b": "89",
            "c": "0",
            "d": "Nothing"
        },
        "answer": "c"
    },
    {
        "question": "What do these lines print?\nfor i in [1, 3, 4, 2]:\n\tprint(i, end=\"-\")",
        "options": {
            "a": "1 2 3 4",
            "b": "1, 3, 4, 2, 0",
            "c": "1--3--4--2",
            "d": "1-3-4-2"
        },
        "answer": "d"
    },
    {
        "question": "What do these lines print?\na = { 'id': 89, 'name': \"John\" }\na.get('age')",
        "options": {
            "a": "'age'",
            "b": "89",
            "c": "12",
            "d": "Nothing"
        },
        "answer": "d"
    },
    {
        "question": "Which of the following data structure in python does not allow duplicates?",
        "options": {
            "a": "Tuple",
            "b": "Set",
            "c": "Dictionary",
            "d": "List"

        "question": "What is setattr() used for?",
        "options": {
            "a": "To access the attribute of the object",
            "b": "To set an attribute",
            "c": "To check if an attribute exists or not",
            "d": "To delete an attribute"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following is true about dictionaries in python?",
        "options": {
            "a": "Dictionaries are ordered",
            "b": "Dictionaries can have duplicate keys",
            "c": "Dictionaries can have mutable values",
            "d": "Dictionaries can be accessed using any index"
        "question": "What will be the output of the following Python program?\n\ni = 0\nwhile i < 5:\n\tprint(i)\ni += 1\nif i == 3:\n\tbreak\nelse:\n\tprint(0)",
        "options": {
            "a": "error",
            "b": "0 1 2 0",
            "c": "0 1 2",
            "d": "none of the mentioned"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code dict(zip(['a', 'b', 'c'], [1, 2, 3]))?",
        "options": {
            "a": "{'a': 1, 'b': 2, 'c': 3}",
            "b": "{1: 'a', 2: 'b', 3: 'c'}",
            "c": "[('a', 1), ('b', 2), ('c', 3)]",
            "d": "{(1, 'a'), (2, 'b'), (3, 'c')}"
        },
        "answer": "a"
    },
    {
        "question": "Which of the following method can be used to add an item to a set?",
        "options": {
            "a": "add()",
            "b": "append()",
            "c": "extend()",
            "d": "insert()"
        },
        "answer": "a"
    },
    {
        "question": "Which of the following methods can be used to remove an item from a set?",
        "options": {
            "a": "remove()",
            "b": "pop()",
            "c": "delete()",
            "d": "discard()"
        "question": "What will be the output of the following Python code?\n\nclass change:\n\tdef __init__(self, x, y, z):\n\tself.a = x + y + z\n\tx = change(1,2,3)\n\ty = getattr(x, 'a')\n\tsetattr(x, 'a', y+1)\n\tprint(x.a)",
        "options": {
            "a": "6",
            "b": "7",
            "c": "0",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "Which of these definitions correctly describes a module?",
        "options": {
            "a": "Any program that reuses code",
            "b": "Defines the specification of how it is to be used",
            "c": "Denoted by triple quotes for providing the specification of certain program elements",
            "d": "Design and implementation of specific functionality to be incorporated into a program"
        },
        "answer": "d"
    },
    {
        "question": "To include the use of functions which are present in the random library, we must use the option:",
        "options": {
            "a": "random.h",
            "b": "import.random",
            "c": "import random",
            "d": "random.random"
        },
        "answer": "c"
    },
    {
        "question": "The output of the following Python code is either 1 or 2.\nimport random\nrandom.randint(1,2)",
        "options": {
            "a": "True",
            "b": "False"
        },
        "answer": "a"
    },
    {
        "question": "Which of the following is true about tuple in python?",
        "options": {
            "a": "Tuple can be modified after creation",
            "b": "Tuple can be used as key in a dictionary",
            "c": "Tuple can be accessed using an index",
            "d": "Tuple can have duplicate"
        "question": "What do these lines print?\na = [5, 7, 9, 11]\na[-1]",
        "options": {
            "a": "-1",
            "b": "[11, 9, 7, 5]",
            "c": "11",
            "d": "7"
        },
        "answer": "c"
    },
    {
        "question": "What do these lines print?\nfor i in range(5, 8):\n    print(i, end=\" \")",
        "options": {
            "a": "5 6 7 8",
            "b": "5 6 7",
            "c": "0 5 6 7",
            "d": "5,6,7"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following methods can be used to open a file in python for writing?",
        "options": {
            "a": "open('filename.txt', 'r')",
            "b": "open('filename.txt', 'w')",
            "c": "open('filename.txt', 'a')",
            "d": "open('filename.txt', 'x')"
        },
        "answer": "b"
    },

        "question": "What does this python program output?\ndef dem(name, age):\n    print(name, age)\ndem(\"Ben\", 25)",
        "options": {
            "a": "25",
            "b": "Ben",
            "c": "Ben 25",
            "d": "error"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following is correct?",
        "options": {
            "a": "defunct(a, b)",
            "b": "def add(a, b):",
            "c": "define add(a + b):",
            "d": "define add(a + b)"
        },
        "answer": "b"
    },
    {
        "question": "What do these lines print?\na = { 'id': 89, 'name': \"John\" }\na.get('age', 0)",
        "options": {
            "a": "'age'",
            "b": "89",
            "c": "0",
            "d": "Nothing"
        },
        "answer": "c"
    },
     {
        "question": "What do these lines print?\nfor i in [1, 3, 4, 2]:\n\tprint(i, end=\"-\")",
        "options": {
            "a": "1 2 3 4",
            "b": "1, 3, 4, 2, 0",
            "c": "1--3--4--2",
            "d": "1-3-4-2"
        },
        "answer": "d"
    },
    {
        "question": "What do these lines print?\na = { 'id': 89, 'name': \"John\" }\na.get('age')",
        "options": {
            "a": "'age'",
            "b": "89",
            "c": "12",
            "d": "Nothing"
        },
        "answer": "d"
    }
]
