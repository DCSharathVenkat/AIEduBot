EduBot - Your Python Teacher
EduBot is a simple Python-based chatbot designed to help users learn about Python programming concepts. Users can ask questions related to Python, and EduBot will provide explanations along with additional resources when available.

Features
Interactive user interface built with Tkinter
Natural language processing to understand user queries
Provides explanations for Python concepts
Displays additional resources as clickable hyperlinks
Requirements
Python 3.x
NLTK
FuzzyWuzzy
Tkinter (usually included with Python installations)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/edubot.git
cd edubot
Install required Python packages:

bash
Copy code
pip install nltk fuzzywuzzy
Download NLTK data:

python
Copy code
import nltk
nltk.download('punkt')
Create a knowledge.py file with your knowledge base:

python
Copy code
knowledge_base = {
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
    }
    # Add more concepts as needed
}
Usage
Run the EduBot application:

bash
Copy code
python edubot.py
Interact with EduBot:

Enter your Python-related questions in the input field.
Click the "Ask" button to get an explanation and additional resources if available.
Click on any provided hyperlinks to open additional resources in your web browser.
Example Questions
What are modules in Python?
Explain Python classes.
Describe Python functions.
Screenshots

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/fooBar).
Commit your changes (git commit -m 'Add some fooBar').
Push to the branch (git push origin feature/fooBar).
Create a new Pull Request.
Contact
For any questions or feedback, please contact dcsharu76@gmail.com.

