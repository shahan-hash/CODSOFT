import re
import random
import wikipedia
from datetime import datetime


def safe_calculate(text):
    try:
        if re.fullmatch(r"[0-9+\-*/().% ]+", text):
            return f"The answer is: {eval(text)}"
    except:
        return None


def wiki_answer(question):
    try:
        results = wikipedia.search(question)

        if not results:
            return "I don't have knowledge about this right now."

        summary = wikipedia.summary(results[0], sentences=2)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:4]
        return "This question can mean different things. Try asking about:\n\n" + "\n".join(options)

    except:
        return "I don't have knowledge about this right now."


def chatbot_response(user_input):
    original = user_input.strip()
    text = original.lower()

    calculation = safe_calculate(text)
    if calculation:
        return calculation

    # Help / wrong spelling help
    if text in ["help", "hellp", "hlp", "options", "menu"] or "what can you do" in text:
        return """
Hello! I am Intellex.

I can help you with:
1. General questions
2. Wikipedia-based information
3. Maths calculations 
4. Study and exam guidance
5. Motivation
6. Jokes
7. Date and time


Just type normally. You don't need special commands.
"""

    # Normal conversation
    elif re.search(r"\b(hi|hello|hey|hii|namaste)\b", text):
        return random.choice([
            "Hello! I am Intellex. How can I help you today?",
            "Hi! Ask me anything.",
            "Hey! I am ready to help you."
        ])

    elif "how are you" in text or "how r u" in text:
        return "I'm doing great! Thanks for asking. How are you?"

    elif "i am fine" in text or "i'm fine" in text or text == "fine":
        return "That's nice to hear! How can I help you?"

    elif "what's up" in text or "whats up" in text:
        return "Not much, just helping users with questions and tasks."

    elif "nice to meet you" in text:
        return "Nice to meet you too!"

    # Identity
    elif "your name" in text or "who are you" in text:
        return "My name is Intellex. I am an intelligent rule-based chatbot created to answer and assist users."

    elif "who made you" in text or "creator" in text:
        return "I was created by Shahan Ahmad as a CODSOFT Artificial Intelligence internship project."

    # Date/time
    elif "time" in text:
        return datetime.now().strftime("Current time is %I:%M %p.")

    elif "date" in text or "today" in text:
        return datetime.now().strftime("Today's date is %d-%m-%Y.")

    # Low marks / exam support
    elif any(phrase in text for phrase in [
        "less marks", "low marks", "bad marks", "failed", "fail",
        "not good marks", "poor marks", "marks are low", "got less marks",
        "i got less marks", "i failed"
    ]):
        return """
I'm sorry to hear that. But low marks are not the end, they are feedback.

You can improve next time by:
1. Checking which topics you lost marks in
2. Practicing previous year questions
3. Making short notes for revision
4. Studying daily in small parts
5. Avoiding only last-night preparation

If you want, tell me the subject and I can help you make a better study plan.
"""

    # Study/exam
    elif "study" in text or "exam" in text or "prepare" in text:
        return """
For better study, follow this:

1. Pick one subject
2. Divide it into small topics
3. Study one topic properly
4. Solve questions from that topic
5. Revise before sleeping

Smart revision is better than only reading again and again.
"""

    # Motivation / natural low feeling
    elif (
        "motivate" in text or
        "motivation" in text or
        "demotivated" in text or
        "i can't do" in text or
        "i cannot do" in text or
        "i am not able" in text
    ):
        return random.choice([
            "Don't stop because one result was bad. Improve one step daily and your next result can be much better.",
            "You don't need to be perfect today. You only need to be better than yesterday.",
            "Every expert was once confused. Keep going."
        ])

    elif any(word in text for word in ["sad", "upset", "tired", "stressed", "depressed"]):
        return "I'm sorry you are feeling this way. Take a small break, breathe, and don't judge your whole future by one bad day."

    elif any(word in text for word in ["happy", "great", "awesome", "good"]):
        return "That's great to hear. Keep going with the same energy!"

    # Joke
    elif "joke" in text:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? Because it had a virus.",
            "Debugging is like being a detective where you are also the criminal."
        ]
        return random.choice(jokes)

    # CODSOFT
    elif "codsoft" in text or "internship" in text:
        return "For CODSOFT, keep your project clean with source code, README, screenshots, and demo video."

    # Thanks / bye
    elif "thank" in text:
        return "You're welcome!"

    elif re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return "Goodbye! Have a great day."

    # Wikipedia fallback
    else:
        return wiki_answer(original)