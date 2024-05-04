import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import knowledge as k
import webbrowser
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Importing functions from your provided code
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize

# Function to preprocess user query
def preprocess_query(query):
    tokens = word_tokenize(query)
    return [word.lower() for word in tokens]

# Function to get potential concepts from knowledge base
def get_potential_concepts(preprocessed_query, kb):
    potential_concepts = []
    for concept in k.knowledge_base.keys():
        if any(word in concept for word in preprocessed_query):
            potential_concepts.append(concept)
    return potential_concepts

# Function to get explanation based on user query
def get_explanation(query):
    preprocessed_query = preprocess_query(query)
    potential_concepts = get_potential_concepts(preprocessed_query, k.knowledge_base)
    if not potential_concepts:
        return "Concept not found in the knowledge base."
    if len(potential_concepts) == 1:
        concept = potential_concepts[0]
        return k.knowledge_base[concept]["answer"], k.knowledge_base[concept].get("additional_resources", None)
    elif potential_concepts:
        best_match_concept = max(potential_concepts, key=lambda concept: len(set(preprocessed_query) & set(concept.split())))
        return k.knowledge_base[best_match_concept]["answer"], k.knowledge_base[best_match_concept].get("additional_resources", None)

# Function to handle user input and display results in GUI
def process_query():
    user_query = query_entry.get()
    explanation, additional_resources = get_explanation(user_query)
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, explanation)
    if additional_resources:
        output_text.insert(tk.END, "\n\nAdditional Resources: ")
        output_text.insert(tk.END, additional_resources, hyperlink)
    output_text.config(state=tk.DISABLED)

# Function to open hyperlink in default web browser
def hyperlink(event):
    webbrowser.open(event.widget.get("current linestart", "current lineend"))

# Function to speak the explanation
def speak_explanation():
    explanation = output_text.get(1.0, tk.END)
    engine.say(explanation)
    engine.runAndWait()

# Create main GUI window
window = tk.Tk()
window.title("EduBot - Your Python Teacher")

# Set style for the GUI
style = ttk.Style()
style.configure("TButton", font=("calibri", 12), padding=10)
style.configure("TLabel", font=("calibri", 12), padding=10)
style.configure("TEntry", font=("calibri", 12), padding=10)

# Input field
query_label = ttk.Label(window, text="Hi! I amEduBot - Your Python Teacher\n\nAsk me a question:") 
query_label.pack(pady=5)
query_entry = ttk.Entry(window, width=50)
query_entry.pack(pady=5)

# Button to trigger query processing
search_button = ttk.Button(window, text="Ask", command=process_query)
search_button.pack(pady=5)

# Output field
output_text = scrolledtext.ScrolledText(window, width=60, height=15, wrap=tk.WORD, font=("calibri"))  
output_text.pack(pady=5)
output_text.config(state=tk.DISABLED)

# Bind hyperlink function to output_text
output_text.tag_configure("hyperlink", foreground="blue", underline=True)
output_text.tag_bind("hyperlink", "<Button-1>", hyperlink)

# Add a "Clear" button
clear_button = ttk.Button(window, text="Clear", command=lambda: [query_entry.delete(0, tk.END), output_text.config(state=tk.NORMAL), output_text.delete(1.0, tk.END), output_text.config(state=tk.DISABLED)])
clear_button.pack(pady=5)

# Add a "Speak" button
speak_button = ttk.Button(window, text="Speak", command=speak_explanation)
speak_button.pack(pady=5)

window.mainloop()