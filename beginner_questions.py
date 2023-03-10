#!/usr/bin/python3

# Store beginner level questions as a list of dictionaries
PROBLEM_SETS = [
    {
        "question": "Which of the following is a correct way to declare a variable in Python?\n",
        "options": {
            "a": "1var = 'Hello World'",
            "b": "var-1 = 'Hello World'",
            "c": "var_1 = 'Hello World'",
            "d": "Var$1 = 'Hello World'"
            },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n\n x = 5 \n y = 2 \n print(x+y)\n print(x-y)\n print(x*y)\n print(x/y)\n",
        "options": {
            "a": "7, 3, 10, 2.5",
            "b": "3, 7, 10, 2.5",
            "c": "7, 3, 10, 2",
            "d": "3, 7, 10, 2"
            },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\n x = 'Hello'\n y = 'World'\n print(x+y)\n",
        "options": {
            "a": "Hello World",
            "b": "HelloWorld",
            "c": "Hello+World",
            "d": "None of the above"
            },
        "answer": "a"
    },
    {
        "question": "Which of the following is the correct syntax to declare a list in Python?\n",
        "options": {
            "a": "list = [1, 2, 3]",
            "b": "list = {1, 2, 3}",
            "c": "list = (1, 2, 3)",
            "d": "list = '1, 2, 3'"
            },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\n x = 5 \n y = 10\n if x>y:\n\tprint('x is greater than y')\nelse:\n\tprint('y is greater than x')\n",
        "options": {
            "a": "x is greater than y",
            "b": "y is greater than x",
            "c": "x and y are equal",
            "d": "Syntax error"
            },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n\n x = 0\n while x < 5:\n\tprint(x)\n\tx+=1\n",
        "options": {
            "a": "0 1 2 3 4",
            "b": "5",
            "c": "Infinite loop",
            "d": "None of the above"
            },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\n for x in range(1,6):\n\tprint(x)",
        "options": {
            "a": "1 2 3 4 5",
            "b": "0 1 2 3 4",
            "c": "6 7 8 9 10",
            "d": "None of the above"
            },
        "answer": "a"
    },
    {
        "question": "What does the 'print()' function do?",
        "options": {
            "a": "It prompts the user to input a value",
            "b": "It adds two numbers together",
            "c": "It displays a message or value on the screen",
            "d": "It converts a value to a string"
        },
        "answer": "c"
    },
    {
        "question": "What is the result of the expression '5 + 7'?",
        "options": {
            "a": "12",
            "b": "13",
            "c": "14",
            "d": "15"
        },
        "answer": "a"
    },
    {
        "question": "What is the correct way to declare a variable in Python?",
        "options": {
            "a": "var x = 5",
            "b": "int x = 5",
            "c": "x = 5",
            "d": "x := 5"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the code 'print(len('hello'))'?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "b"
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
                 "": "Hello",
                 "c": "sybntax error"
                 },
             "answer": "a"
             },
             {
             "question": "what will this line print?\n q = True\n p = False\n result = q and p\n print(result)",
             "options": {
                 "a": "True",
                 "b": "False",
                 "c": "Error"
                 },
             "answer": "b"
             },
 {
             "question": "what will this line print?\n w = 9\n z = 6\n result = w < z\n print(result)",
             "options": {
                 "a": "True",
                 "b": "False",
                 "c": "Error"
                 },
             "answer": "b"
             },
              {
             "question": "what will this line print?\n age = 50\n print("My age is "+ age)",
             "options": {
                 "a": "My age is 50",
                 "b": "My age",
                 "c": "syntax error"
                 },
             "answer": "c"
             },
            {
                "question": "what will this line print?\n for r in range(7):\n print(r)",
             "options": {
                 "a": "0 1 2 3 4 5 6",
                 "b": "0 1 2 3 4 5 6 7",
                 "c": "None of the above"
                 },
             "answer": "a"
             },
             {
              "question": "what will this line print?\n my_list = [1, 2, 3, 4, 5]\n for my in my_list:\n\t print(my)",
             "options": {
                 "a": "1 2 3 4 5",
                 "b": "[1, 2, 3, 4, 5]",
                 "c": "syntax error"
                 },
             "answer": "a"
             },
             {
             "question": "what will this line print?\n x = 15\n y = 5\n if x > y:\n\t print("x is number 24")\n else:\n\t print("y is number 25")",
             "options": {
                 "a": "x is number 24",
                 "b": "y is number 25",
                 "c": "syntax error"
                 },
             "answer": "a"
             },
              {
            "question": "what will this line print?\n first_list = [1 2 3 4 5]\n print(len(first_list))",
             "options": {
                 "a": "1",
                 "b": "5",
                 "c": "syntax error"
                 },
             "answer": "b"
             },
               {
           "question": "what will this line print?\n x = 8\n y = 5\n result = x - y\n print(result)",
             "options": {
                 "a": "3",
                 "b": "5",
                 "c": "syntax error"
                 },
             "answer": a    
             },

]

