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
        "question": "What will be the output of the following Python code?

class change:
    def __init__(self, x, y, z):
        self.a = x + y + z
 
x = change(1,2,3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
print(x.a)",
        "options": {
            "a": "6",
            "b": "7",
            "c": "0",
            "d": "Error"
        },
        "answer": "b"
    },
     {
        "question": "What is a generator in Python?",
        "options": {
            "a": "The function that generates random numbers of specified count",
            "b": "The function that generates an error when a warning occurs",
            "c": "The function that gives a statement as output rather than a return",
            "d": "The function that returns a generic object"
        },
        "answer": "c"
        },
      {
        "question": "What is the output of the below code?

def fun(arr):

    arr=arr[::-1]

arr=[1,2,3,4,5]

fun(arr)

print(arr)",
        "options": {
            "a": "[1,2,3,4,5]",
            "b": "[5,4,3,2,1]",
            "c": "[]",
            "d": "NameError"
        },
        "answer": "a"
        },
       {
        "question": "Which of the following is true about the stack?",
        "options": {
            "a": "Stack following LIFO order",
            "b": "The time complexity to push and pop an element is O(1)",
            "c": "It is a linear data Structure",
            "d": "All of the above"
        },
        "answer": "d"
        },
]
