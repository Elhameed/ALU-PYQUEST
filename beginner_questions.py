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

]
