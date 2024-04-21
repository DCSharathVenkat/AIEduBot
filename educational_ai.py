import nltk
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz

# Knowledge base
knowledge_base = {
    "dictionaries": {
    "question": [
        "What are dictionaries in Python?",
        "Define dictionaries",
    ] ,
    "answer": "Dictionaries are unordered collections of key-value pairs. Keys are unique and used to access the corresponding values. Dictionaries are useful for storing and organizing data based on keys.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.programiz.com/python/dictionary/"
  },

  "conditional statements": {
    "question": "What are conditional statements in Python?",
    "answer": "Conditional statements allow you to control the flow of your program based on certain conditions. They use keywords like 'if', 'elif', and 'else' to execute different code blocks depending on whether a condition is True or False.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.w3schools.com/python/python_conditional_statements.asp"
  },

  "strings": {
    "question": "What are strings in Python?",
    "answer": "Strings are sequences of characters. They are used to represent text data. Strings are immutable (their content cannot be changed after creation).",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.tutorialspoint.com/python/python_strings.htm"
  },


  "operators": {
    "question": "What are operators in Python?",
    "answer": "Operators are special symbols that perform operations on values. Python has various operators like arithmetic operators (+, -, *, /), comparison operators (==, !=, <, >), and logical operators (and, or, not).",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.guru99.com/python-operators.htm"
  },

  "modules": {
    "question": "What are modules in Python?",
    "answer": "Modules are reusable Python code files. They contain functions, classes, and variables that can be imported and used in other Python scripts. Modules help in code organization and reusability.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://www.datacamp.com/tutorial/modules-in-python"
  },

  "classes": {
    "question": "What are classes in Python?",
    "answer": "Classes are blueprints for creating objects. They define properties (attributes) and functionalities (methods) that objects of that class will inherit. Classes are fundamental for object-oriented programming in Python.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://www.tutorialspoint.com/python/python_classes.htm"
  },

"input/output": {
    "question": "How to get user input and print output in Python?",
    "answer": "Python provides functions to get user input (using the 'input' function) and display output (using the 'print' function). These functions are essential for interacting with users in your programs.",
    "difficulty_level": "beginner",
    "additional_resources": "Link",
},

"tuples": {
    "question": "What are tuples in Python?",
    "answer": "Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation. They are ordered collections of items and can store different data types.",
    "difficulty_level": "beginner",
    "additional_resources": "https://www.tutorialspoint.com/python/python_tuples.htm"
  },

  "sets": {
    "question": "What are sets in Python?",
    "answer": "Sets are unordered collections of unique elements. They are useful for tasks like membership testing and eliminating duplicate entries from other collections.",
    "difficulty_level": "beginner",
    "additional_resources": "https://realpython.com/python-sets/"
  },

  "file handling": {
    "question": "What is file handling in Python?",
    "answer": "File handling in Python allows you to work with files on the filesystem. You can open, read, write, and close files using built-in functions and methods.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"
  },

  "exception handling": {
    "question": "What is exception handling in Python?",
    "answer": "Exception handling is a mechanism to deal with runtime errors in Python. It allows you to catch and handle exceptions gracefully, preventing your program from crashing.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/python-exceptions/"
  },

  "generators": {
    "question": "What are generators in Python?",
    "answer": "Generators are functions that allow you to generate a sequence of values lazily. They produce values one at a time and are memory efficient compared to lists.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/introduction-to-python-generators/"
  },

  "recursion": {
    "question": "What is recursion in Python?",
    "answer": "Recursion is a programming technique where a function calls itself in its own definition. It is often used to solve problems that can be broken down into smaller, similar subproblems. Recursion involves breaking down a problem into smaller instances of the same problem until the base case is reached.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://www.geeksforgeeks.org/recursion-in-python/"
},

"lambda_functions": {
    "question": "What are lambda functions in Python?",
    "answer": "Lambda functions, also known as anonymous functions, are small, inline functions defined using the 'lambda' keyword. They are typically used for short, simple operations where a full function definition is not required. Lambda functions can take any number of arguments but can only have one expression.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/python-lambda/"
},

"list_comprehensions": {
    "question": "What are list comprehensions in Python?",
    "answer": "List comprehensions provide a concise way to create lists in Python. They allow you to generate new lists by applying an expression to each item in an existing iterable. List comprehensions are often more readable and efficient than traditional looping techniques.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions"
},

"decorators": {
    "question": "What are decorators in Python?",
    "answer": "Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their actual code. Decorators are implemented using functions that take another function as input and return a new function that usually enhances the input function in some way.",
    "difficulty_level": "advanced",
    "additional_resources": "https://realpython.com/primer-on-python-decorators/"
},

"OOP": {
    "question": "What is object-oriented programming (OOP) in Python?",
    "answer": "Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to organize code. In Python, everything is an object, and you can create your own custom objects by defining classes. OOP concepts include encapsulation, inheritance, and polymorphism.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/python3-object-oriented-programming/"
},

"multithreading": {
    "question": "What is multithreading in Python?",
    "answer": "Multithreading is a programming technique that allows multiple threads of execution to run concurrently within a single process. In Python, multithreading is used to perform concurrent tasks, but due to the Global Interpreter Lock (GIL), it may not fully utilize multiple CPU cores for CPU-bound tasks.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/intro-to-python-threading/"
},

"multiprocessing": {
    "question": "What is multiprocessing in Python?",
    "answer": "Multiprocessing is a programming technique that allows you to run multiple processes concurrently, taking advantage of multiple CPU cores and bypassing the Global Interpreter Lock (GIL). In Python, the 'multiprocessing' module provides support for multiprocessing.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://docs.python.org/3/library/multiprocessing.html"
},

"regular expressions (regex)": {
    "question": "What are regular expressions (regex) in Python?",
    "answer": "Regular expressions are sequences of characters that define a search pattern. They are used for pattern matching and text manipulation tasks. Python provides the 're' module for working with regular expressions.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/regex-python/"
},

"data analysis with pandas": {
    "question": "What is data analysis with pandas in Python?",
    "answer": "Data analysis with pandas involves using the pandas library in Python to manipulate and analyze structured data. Pandas provides powerful data structures like DataFrames and Series, along with functions for data cleaning, transformation, aggregation, and visualization.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html"
},

"recursion": {
    "question": "What is recursion in programming?",
    "answer": "Recursion is a programming technique where a function calls itself in order to solve a problem. It involves breaking down a problem into smaller subproblems that are similar to the original problem. Recursion is often used in algorithms dealing with tasks like tree traversal, factorial calculation, and solving mathematical problems.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/python-thinking-recursively/"
},

"regular expressions": {
    "question": "What are regular expressions in Python?",
    "answer": "Regular expressions (regex) are sequences of characters that define a search pattern. They are used for pattern matching and string manipulation tasks. Python provides a 're' module for working with regular expressions, allowing you to search, match, and manipulate text based on specified patterns.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://docs.python.org/3/library/re.html"
},

"decorators": {
    "question": "What are decorators in Python?",
    "answer": "Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their code. Decorators are implemented as functions themselves, and they take another function as input and return a new function that usually extends the behavior of the input function.",
    "difficulty_level": "intermediate",
    "additional_resources": "https://realpython.com/primer-on-python-decorators/"
},

"asynchronous programming": {
    "question": "What is asynchronous programming in Python?",
    "answer": "Asynchronous programming is a programming paradigm that allows tasks to run concurrently, enabling better utilization of resources and improved performance. In Python, asynchronous programming is commonly implemented using the 'asyncio' module, which provides primitives for writing asynchronous code using coroutines.",
    "difficulty_level": "advanced",
    "additional_resources": "https://realpython.com/async-io-python/"
},
    "functions": {
        "question": "What are functions in Python?",
        "answer": "Functions are blocks of code that can be called multiple times from different parts of a program. They can take arguments and return values.",
        "difficulty_level": "intermediate",
        "additional_resources": "(link unavailable)"
    }
}

def preprocess_query(query):
    #print("Preprocessing query...")
    tokens = word_tokenize(query)
    return [word.lower() for word in tokens]

def get_potential_concepts(preprocessed_query, knowledge_base):
    #print("Getting potential concepts...")
    potential_concepts = []
    for concept in knowledge_base.keys():
        if any(word in concept for word in preprocessed_query):
            potential_concepts.append(concept)
    return potential_concepts

def get_explanation(query):
    #print("Inside get_explanation function")
    # Preprocess the user query
    preprocessed_query = preprocess_query(query)
   # print("Preprocessed query:", preprocessed_query)

    # Print keys of the knowledge base for debugging
    #print("Knowledge base keys:", knowledge_base.keys())

    # Identify potential concepts in the knowledge base that match the query
    potential_concepts = get_potential_concepts(preprocessed_query, knowledge_base)
    #print("Potential concepts:", potential_concepts)

    # If no potential concepts found, return a message
    if not potential_concepts:
        print("Concept not found in the knowledge base.")
        return

    # If a perfect match is found, return the explanation directly
    if len(potential_concepts) == 1:
        concept = potential_concepts[0]
        #print("Perfect match found")
        return knowledge_base[concept]  # Return the entire concept dictionary

    # If no perfect match, identify the concept with the most matching words (basic approach)
    elif potential_concepts:
        best_match_concept = max(potential_concepts, key=lambda concept: len(set(preprocessed_query) & set(concept.split())))
        #print("Best match found")
        return knowledge_base[best_match_concept]  # Return the entire concept dictionary

def main():
    print("Script started")
    while True:
        user_query = input("Enter a question about programming (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break
        
        concept_info = get_explanation(user_query)
        if concept_info:
            explanation = concept_info["answer"]
            difficulty_level = concept_info["difficulty_level"]
            additional_resources = concept_info.get("additional_resources", None)
            
            print(f"\nExplanation for {user_query}:")
            print(explanation)
            if additional_resources:
                print(f"\nAdditional Resources: {additional_resources}")

if __name__ == "__main__":
    main()