# Intellex - Intelligent Rule-Based Chatbot

Intellex is an intelligent rule-based chatbot developed for the CODSOFT Artificial Intelligence Internship. It responds to user inputs using predefined rules, if-else conditions, and pattern matching techniques. It also includes Wikipedia search as a fallback feature for general knowledge questions.

## Features

* Rule-based chatbot responses
* Pattern matching using Python
* Streamlit chat interface
* General conversation handling
* Direct mathematical calculation
* Study and exam guidance
* Motivational responses
* Jokes
* Date and time response
* Wikipedia-based knowledge fallback
* Chat history support

## Technologies Used

* Python
* Streamlit
* Wikipedia Python Library
* Regular Expressions

## Project Structure

```text
Advanced_Rule_Based_Chatbot/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/CODSOFT.git
```

2. Open the project folder:

```bash
cd CODSOFT/Advanced_Rule_Based_Chatbot
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
venv\Scripts\activate
```

5. Install required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
streamlit run app.py
```

## Sample Inputs

```text
hello
simple math calculation
what is python(wikipedia information)
provide motivation
tell me a joke
what is the time
who made you
```

## About the Chatbot

Intellex first checks user input using predefined rules and pattern matching. If the input matches a known rule, it gives a predefined response. If no rule matches, it searches Wikipedia and returns a short summary.

## CODSOFT Task

Task: Build a simple chatbot that responds to user inputs based on predefined rules using if-else statements or pattern matching techniques.

This project follows the task requirement and also adds extra features like Streamlit UI, calculator support, study guidance, and Wikipedia fallback.

## Author

Shahan Ahmad
