#!/usr/bin/python3

# advanced_questions.py

# Store advanced level questions as a list of dictionaries
PROBLEM_SETS = [
    {
        "question": "What is the output of the following code?\n\nmy_list = [1, 2, 3, 4, 5]\nnew_list = [x for x in my_list if x % 2 == 0]\nprint(new_list)",
        "options": {
            "a": "[2, 4]",
            "b": "[1, 3, 5]",
            "c": "[2, 4, 6]",
            "d": "[1, 2, 3, 4, 5]"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\ndef my_func(a, b, c):\n    print(a, b, c)\n\nargs = (1, 2, 3)\nmy_func(*args)",
        "options": {
            "a": "1 2 3",
            "b": "(1, 2, 3)",
            "c": "TypeError: my_func() takes 3 positional arguments but 4 were given",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\ndef my_func(a, b, c=0):\n    print(a, b, c)\n\nmy_func(1, 2)",
        "options": {
            "a": "1 2 0",
            "b": "1 2",
            "c": "TypeError: my_func() missing 1 required positional argument: 'b'",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\nimport re\nmy_string = 'The quick brown fox jumps over the lazy dog'\nresult = re.findall('[aeiou]', my_string)\nprint(result)",
        "options": {
            "a": "['a', 'e', 'i', 'o', 'u']",
            "b": "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']",
            "c": "['aeiou']",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\nmy_dict = {1: 'one', 2: 'two', 3: 'three'}\nfor key, value in my_dict.items():\n    print(key, value)",
        "options": {
            "a": "1 'one', 2 'two', 3 'three'",
            "b": "1 one, 2 two, 3 three",
            "c": "['one', 'two', 'three']",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "b"
    }
    {
        "question": "What is the difference between the print() function and the return statement in Python?",
        "options": {
            "a": "print() displays output to the console, while return statement returns a value from a function",
            "b": "print() is used for debugging purposes, while return statement is used to terminate a loop",
            "c": "print() and return statement are interchangeable and can be used interchangeably",
            "d": "print() and return statement are not valid functions in Python"
        },
        "answer": "a"
    }
    {
        "question": "What is the purpose of the urllib module in Python?",
        "options": {
            "a": "To perform HTTP requests and handle responses",
            "b": "To generate random numbers",
            "c": "To manipulate strings",
            "d": "To perform mathematical operations"
        },
        "answer": "a"
    }
    {
        "question": "What is the purpose of test-driven development (TDD) in software development?",
        "options": {
            "a": "To ensure that code is thoroughly tested before it is released to production",
            "b": "To write tests after the code has been written to ensure it works properly",
            "c": "To write code without testing and fix any bugs that arise later",
            "d": "To write code quickly without worrying about testing"
        },
        "answer": "a"
    }
    {
        "question": "What is object-relational mapping (ORM) in Python?",
        "options": {
            "a": "A technique for mapping objects in Python to relational database tables",
            "b": "A technique for mapping Python functions to RESTful APIs",
            "c": "A technique for mapping Python modules to object-oriented programming (OOP) concepts",
            "d": "A technique for mapping Python scripts to network protocols"
        },
        "answer": "a"
    }
    {
        "question": "What is the difference between the input() function and the raw_input() function in Python 2.x?",
        "options": {
            "a": "The input() function returns a string, while the raw_input() function returns the input as it is typed",
            "b": "The raw_input() function is not a valid function in Python 2.x",
            "c": "The input() function is not a valid function in Python 2.x",
            "d": "The input() and raw_input() functions are interchangeable and can be used interchangeably in Python 2.x"
        },
        "answer": "a"
    }
    {
        "question": "Which of the following is a valid way to open a file named \"example.txt\" in read mode?",
        "options": {
            "a": "file = open(\"example.txt\", mode=\"w\")",
            "b": "file = open(\"example.txt\", mode=\"r+\")"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n\ndef greet(name):\n    return f\"Hello, {name}!\"\n\nprint(greet(\"Alice\"))",
        "options": {
            "a": "Hello, Alice!",
            "b": "Hello, !",
            "c": "TypeError: greet() missing 1 required positional argument: 'name'",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n lst = [1, 2, 3, 4, 5]\n new_lst = [num * 2 for num in lst if num % 2 == 0]\n print(new_lst)",
        "options": {
            "a": "[2, 4, 6, 8, 10]",
            "b": "[4, 8]",
            "c": "[2, 6, 10]",
            "d": "[1, 2, 3, 4, 5]"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following is not a built-in function in Python?",
        "options": {
            "a": "sum()",
            "b": "len()",
            "c": "sort()",
            "d": "range()"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n a = [1, 2, 3]\n b = a\n b[0] = 0\n print(a)",
        "options": {
            "a": "[0, 2, 3]",
            "b": "[1, 2, 3]",
            "c": "[0, 1, 2, 3]",
            "d": "[1, 0, 2, 3]"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n class MyClass:\n\t def init(self, num):\n\t\t self.num = num\n a = MyClass(5)\n b = MyClass(10)\n print(a.num + b.num)",
        "options": {
            "a": "15",
            "b": "'5 10'",
            "c": "TypeError",
            "d": "AttributeError"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n def my_func(a, b, c, d):\n\t print(a, b, c, d)\n lst = [1, 2, 3, 4]\n my_func(*lst)",
        "options": {
            "a": "TypeError",
            "b": "1 2 3 4",
            "c": "4 3 2 1",
            "d": "1 4 2 3"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n def my_func(a, b=2, c=3):\n\t print(a, b, c)\n my_func(1, c=4)",
        "options": {
            "a": "1 2 3",
            "b": "1 3 4",
            "c": "1 2 4",
            "d": "SyntaxError"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following is true about Python's Global Interpreter Lock (GIL)?",
        "options": {
            "a": "It allows multiple threads to execute Python code simultaneously.",
            "b": "It prevents deadlocks from occurring in Python programs.",
            "c": "It ensures that only one thread executes Python bytecode at a time.",
            "d": "It prevents race conditions from occurring in Python programs."
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n def my_gen(n):\n\t for i in range(n):\n\t\t yield i\n gen = my_gen(3)\n print(next(gen), next(gen), next(gen), next(gen))",
        "options": {
            "a": "0 1 2 StopIteration",
            "b": "0 1 2 None",
            "c": "0 1 2 TypeError",
            "d": "SyntaxError"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n x = 10\n y = 20\n x, y = y, x\n print(x, y)",
        "options": {
            "a": "10 20",
            "b": "20 10",
            "c": "SyntaxError",
            "d": "TypeError"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n def my_func(x):\n\t if x % 2 == 0:\n\t\t return True\n\t else:\n\t\t return False\n lst = [1, 2, 3, 4, 5]\n new_lst = filter(my_func, lst)\n print(list(new_lst))",
        "options": {
            "a": "[1, 3, 5]",
            "b": "[2, 4]",
            "c": "[False, True, False, True, False]",
            "d": "TypeError"
        },
        "answer": "b"
    },
        "question": "Which of the following statements is true about Python's asyncio library?",
        "options": {
            "a": "It allows multiple threads to execute in parallel",
            "b": "It is used for parallel processing of CPU-bound tasks",
            "c": "It is based on the concept of coroutines",
            "d": "It is not compatible with Python 3"
        },
        "answer": "c"
    }
]
