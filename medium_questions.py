#!/usr/bin/python3

PROBLEM_SETS = [
    {
        "question 1": "What is the output of the following code?\n\n class Animal:\n\t def __init__(self, name):\n\t self.name = name\n\n class Dog(Animal):\n\tdef bark(self):\n\tperson1 = Person("John", 25)\n print(person1.name)\n",
        "options": {
            "a": "age 25",
            "b": "john 25",
            "c": "John",
            "d": "None of the above"
        },
        "answer": "c"
    },
    {
        "question2": "What is the output of the following code?\n\n class Animal:\n\t def __init__(self, name):\n\t self.name = name\n\n class Dog(Animal):\n\tdef bark(self):\n\tprint("Woof!")\n\nmy_dog = Dog("Fido")\nprint(my_dog.name)\nmy_dog.bark()\n",
        "options": {
            "a": "Woof",
            "b": "error",
            "c": "Fido",
            "d": " Woof! Fido"
        },
        "answer": "d"
    },
    {
        "question 3": "How do I use  functions in Python?\n\n def add_numbers(x, y):\n\treturn x + y\n\nresult = add_numbers(5, 7)\nprint(result)\n",
        
        "output": "12"
    },
    {
        "question 4": "How can I deal with modules in Python?\n\ndef greet(name):\n\t rint("Hello, " + name + "!")\n\nimport mymodule\n\nmymodule.greet("Alice")\n",
       
        "output": "Hello, Alice!"
    },
    {
        "question 5": "How do I read and write files in Python?\n\nwith open("myfile.txt", "w") as f:\n\tf.write("Hello, World!")\n\nwith open("myfile.txt", "r") as f:\n\tdata = f.read()\nprint(data)\n",
      
        "output": "Hello, World!"
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
    }
]
