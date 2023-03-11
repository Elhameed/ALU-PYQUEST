#!/usr/bin/python3

# Store beginner level questions as a list of dictionaries
PROBLEM_SETS = [
    {
        "question 1": "Which example of a simple programm in Python?\n",

        "answer": "print("Hello, World!") >>Hello, World!"
    },
    {
        "question 2": "How can I use variables in python?\n\n",
        
        "answer": "
         "x = 5",
         "y = 10",
         "z = x + y",
         "print(z)",
 # Output: 15"
    },
    {
        "question 3": "how do I use lists in Python?\n\n my_list = [1, 2, 3, 4, 5]'\n my_list.append(6)'\n print(my_list)\n",
    
        "output": "[1, 2, 3, 4, 5, 6]"
    },
    {
        "question 4": "How do I access individual elements in a list in Python?\n\n my_list = [1, 2, 3, 4, 5]'\n my_list.append(6)'\n print(my_list[0])\n",
       
        "output": "1"
    },
    {
        "question 5": "How do I add elements to a list in Python?\n\n list = ["apple", "banana", "cherry"] \n list.append("orange")\n if x>y:\nlist.extend(["grape", "kiwi"])\nprint(list)\n",
        
        "output": " ["apple", "banana", "cherry", "orange", "grape", "kiwi"]"
    },
    {
        "question 6": "How do I remove elements from a list in Python?\n\n list = ["apple", "banana", "cherry"]\n list.remove("banana")\nprint(list)\n",
        "output": "["apple", "cherry"]"
    },
    {
        "question 7": "How do I sort a list in Python?\n\n list = [3, 1, 4, 1, 5, 9, 2, 6, 5]\n sorted_list = sorted(list)\n print(sorted_list)\n",
       
        "output": "[1, 1, 2, 3, 4, 5, 5, 6, 9]"
    },
    {
        "question 8": "How do I use conditional statement in Python?\n\n x = 5\n\n if x > 0:\n\t  print("x is positive")\n else:\n\t print("x is not positive")\n",
     
        "output": "x is positive"
    },
    {
        "question 9": "How do I check if an element is in a list in Python?\n\n list = ["apple", "banana", "cherry"]\n if "banana" in list:\n\t print("Element found!")\n else:\n\t print("Element not found!")\n",
       
        "output": "Element found!"
    },
    {
        "question 10": "How to use loop in Python?\n\n for i in range(5):\n\t print(i)\n",
        
        "output": "0 1 2 3 4"
    },
    {
        "question": "What is the correct way to define a function in Python?",
        "options": {
            "a": "function myFunction():",
            "b": "def myFunction():",
            "c": "def myFunction:",
            "d": "myFunction():"
        },
        "answer": "b"
    },
    {
        "question": "Why are local variable names beginning with an underscore discouraged?",
        "options": {
            "a": " they are used to indicate a private variables of a class",
            "b": "they confuse the interpreter",
            "c": "they are used to indicate global variables",
            "d": "they slow down execution"
        },
        "answer": "a"
    },
    {
        "question": "what will this line print?\n hub = 1\n if hub < 3:\n\t print('Less than 3')\n else:\n\t print('Greater that or equal to 3')",
        "options": {
            "a": "Less than 3",
            "b": "Greater than or equal to 3",
            "c": "syntax error",
        },
        "answer": "a"
    },
    {
        "question": "what will this line print?\n name = "Adam"\n print("Hello, "+name)\n",
        "options": {
            "a": "Hello Adam",
            "b": "Hello",
            "c": "sybntax error"
        },
        "answer": "a"
    },
    {
        "question": "What will be the output of the following code?\nx = 10\nif x > 5:\n print('x is greater than 5')\nelse:\n print('x is less than or equal to 5')",
        "options": {
            "a": "x is greater than 5",
            "b": "x is less than or equal to 5",
            "c": "Syntax error",
            "d": "None of the above"
        },
        "answer": "a"
    }
    {
        "question": "What will be the output of the following code?\nage = 20\nif age >= 18 and age <= 25:\n print('Age is between 18 and 25')\nelse:\n print('Age is not between 18 and 25')",
        "options": {
            "a": "Age is between 18 and 26",
            "b": "Age is between 18 and 25",
            "c": "Syntax error",
            "d": "None of the above"
        },
        "answer": "b"
    }
    {
        "question": "What keyword would you use to add an alternative condition to an if statement?",
        "options": {
            "a": "else if",
            "b": "elseif",
            "c": "elif",
            "d": "None of the above"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code:\n\n x = 6\n y = 2\n print(x ** y)\n print(x // y)",
        "options": {
            "a": "66\n 0",
            "b": "36\n 0",
            "c": "66\n 3",
            "d": "36\n 3"
        },
        "answer": "d"
    },
    {
        "question": "Find the output of the given Python program?\n\n a = 25\n if a < 15:\n\t print("Hi")\n elif a <= 30:\n\t print("Hello")\n else:\n\t print("Know Program")",
        "options": {
            "a": "Hi",
            "b": "Hello",
            "c": "Know Program",
            "d": "Compiled successfully, No output"
        },
        "answer": "b"
    },
    {
        "question": "Select the correct output of the following String operations\nstr1 = 'Welcome'\nprint (str1[:6] + ' John')",
        "options": {
            "a": "Welcome John",
            "b": "WelcomJohn",
            "c": "Welcom John",
            "d": "None of the above"
        },
        "answer": "a"
    },
    {
        "question": "Guess the correct output of the following String operations\nstr1 = 'Welcome'\nprint(str1*2)",
        "options": {
            "a": "WelcomeWelcome",
            "b": "TypeError unsupported operand type(s)",
            "c": "Welcome",
            "d": "Welcome2"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following\nl = [None] * 10\nprint(len(l))",
        "options": {
            "a": "10",
            "b": "0",
            "c": "Syntax Error"
        "question": "What does pip stand for python?",
        "options": {
            "a": "Pip Installs Python",
            "b": "Pip Installs Packages",
            "c": "Preferred Installer Program",
            "d": "All of the mentioned"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following would give an error?",
        "options": {
            "a": "list1 = []",
            "b": "list1 = [] * 3",
            "c": "list1 = [2, 8, 7]",
            "d": "None of the above"
        "question": "What will be the output of the following Python code?\n\n>>> str1 = 'hello'\n>>> str2 = ','\n>>> str3 = 'world'\n>>> str1[-1:]",
        "options": {
            "a": "olleh",
            "b": "hello",
            "c": "h",
            "d": "o"
        },
        "answer": "d"
    },
    {
        "question": "Suppose list1 is [1, 3, 2], What is list1 * 2?",
        "options": {
            "a": "[2, 6, 4]",
            "b": "[1, 3, 2, 1, 3]",
            "c": "[1, 3, 2, 1, 3, 2]",
            "d": "[1, 3, 2, 3, 2, 1]"
        },
        "answer": "c"
    },
    {
        "question": "Which one of the following is a valid Python if statement.",
        "options": {
            "a": "if a >= 2:",
            "b": "if (a >= 2)",
            "c": "if (a => 22)",
            "d": "if a >= 22"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following assignment operator?\n y = 10\n x = y += 2\n print(x)",
        "options": {
            "a": "12",
            "b": "10",
            "c": "8",
            "d": "Syntax error"
        },
        "answer": "d"
        "question": "Suppose listExample is [‘h’,’e’,’l’,’l’,’o’], what is len(listExample)?",
        "options": {
            "a": "5",
            "b": "4",
            "c": "None",
            "d": "Error"
        },
        "answer": "a"
    }
]
