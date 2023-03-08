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
]
