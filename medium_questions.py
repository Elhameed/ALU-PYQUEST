#!/usr/bin/python3

PROBLEM_SETS = [
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
        "question": "What do these lines print?
?\n\nclass User:\n\tid = 1:\n\n\n User.id = 98\n\nu = User\nu.id = 89\nprint(u.id)",
        "options": {?",
        "options": {
            "a": "89",
            "b": "1",
            "c": "none",
            "d": "100"
        },
        "answer": "89"
    }
]
