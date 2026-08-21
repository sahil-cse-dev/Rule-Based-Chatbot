# ============================================================
# CodeBot - Rule-Based AI Chatbot
# CodeOrbit Tech - Artificial Intelligence Internship
# Task 1: Rule-Based Chatbot
# ============================================================

import re
from datetime import datetime


# ------------------------------------------------------------
# Function 1: Clean the user's input
# ------------------------------------------------------------
def clean_input(user_input):
    """
    Converts input to lowercase and removes punctuation.
    This makes keyword matching easier.
    """

    user_input = user_input.lower()
    user_input = re.sub(r"[^\w\s]", "", user_input)

    return user_input.strip()


# ------------------------------------------------------------
# Function 2: Check whether a keyword exists
# ------------------------------------------------------------
def contains_any(message, keywords):
    """
    Returns True if any keyword from the list
    exists in the user's message.
    """

    return any(keyword in message for keyword in keywords)


# ------------------------------------------------------------
# Function 3: Generate chatbot response
# ------------------------------------------------------------
def chatbot_response(user_input):

    message = clean_input(user_input)

    # --------------------------------------------------------
    # Exit commands
    # --------------------------------------------------------
    if message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Thanks for chatting with CodeBot. 👋"

    # --------------------------------------------------------
    # Greetings
    # --------------------------------------------------------
    if contains_any(
        message,
        ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    ):
        return "Hello! 👋 I'm CodeBot. How can I help you today?"

    # --------------------------------------------------------
    # Asking chatbot's name
    # --------------------------------------------------------
    if "your name" in message or "who are you" in message:
        return "My name is CodeBot. I am a rule-based AI chatbot."

    # --------------------------------------------------------
    # Asking how chatbot is doing
    # --------------------------------------------------------
    if "how are you" in message or "how r you" in message:
        return "I'm doing great! Thanks for asking. 😊"

    # --------------------------------------------------------
    # Asking what chatbot can do
    # --------------------------------------------------------
    if "what can you do" in message or "your features" in message:
        return (
            "I can respond to greetings, answer basic questions, "
            "tell you the date and time, tell jokes, and explain "
            "how I work."
        )

    # --------------------------------------------------------
    # Help
    # --------------------------------------------------------
    if "help" in message:
        return (
            "\nYou can ask me things like:\n"
            "  • Hello\n"
            "  • What is your name?\n"
            "  • How are you?\n"
            "  • What can you do?\n"
            "  • What time is it?\n"
            "  • What is today's date?\n"
            "  • Tell me a joke\n"
            "  • What is AI?\n"
            "  • How do you work?\n"
            "  • Tell me about Python\n"
            "  • Bye"
        )

    # --------------------------------------------------------
    # Current time
    # --------------------------------------------------------
    if "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. 🕐"

    # --------------------------------------------------------
    # Current date
    # --------------------------------------------------------
    if "date" in message or "today" in message:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}. 📅"

    # --------------------------------------------------------
    # How the chatbot works
    # --------------------------------------------------------
    if (
        "how do you work" in message
        or "how you work" in message
        or "how were you made" in message
    ):
        return (
            "I work using predefined rules and keyword matching. "
            "I clean your input, check it against my rules, and "
            "return the response associated with the matching rule."
        )

    # --------------------------------------------------------
    # AI question
    # --------------------------------------------------------
    if "what is ai" in message or "artificial intelligence" in message:
        return (
            "Artificial Intelligence, or AI, is the field of creating "
            "computer systems that can perform tasks that normally "
            "require human intelligence, such as understanding language, "
            "recognizing images, and making decisions."
        )

    # --------------------------------------------------------
    # Python question
    # --------------------------------------------------------
    if "what is python" in message or "tell me about python" in message:
        return (
            "Python is a popular high-level programming language known "
            "for its simple syntax. It is widely used in web development, "
            "data science, automation, AI, and machine learning."
        )

    # --------------------------------------------------------
    # Programming question
    # --------------------------------------------------------
    if "programming" in message or "coding" in message:
        return (
            "Programming is the process of writing instructions that "
            "tell a computer how to perform a task."
        )

    # --------------------------------------------------------
    # Machine Learning question
    # --------------------------------------------------------
    if "machine learning" in message:
        return (
            "Machine Learning is a branch of AI where computers learn "
            "patterns from data and use those patterns to make "
            "predictions or decisions."
        )

    # --------------------------------------------------------
    # Joke
    # --------------------------------------------------------
    if "joke" in message:
        return (
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs! 🐛😂"
        )

    # --------------------------------------------------------
    # Thank you
    # --------------------------------------------------------
    if contains_any(message, ["thank you", "thanks", "thank"]):
        return "You're welcome! 😊"

    # --------------------------------------------------------
    # Positive response
    # --------------------------------------------------------
    if contains_any(message, ["good", "great", "awesome", "nice"]):
        return "That's great to hear! 😄"

    # --------------------------------------------------------
    # Negative response
    # --------------------------------------------------------
    if contains_any(message, ["sad", "bad", "upset", "angry"]):
        return (
            "I'm sorry to hear that. I hope things get better soon. "
            "Is there anything you'd like to talk about?"
        )

    # --------------------------------------------------------
    # Fallback response
    # --------------------------------------------------------
    return (
        "I'm sorry, I don't understand that yet. 🤔\n"
        "Type 'help' to see what I can answer."
    )


# ------------------------------------------------------------
# Function 4: Main chatbot program
# ------------------------------------------------------------
def main():

    print("=" * 60)
    print("              🤖 CODEBOT")
    print("          RULE-BASED AI CHATBOT")
    print("=" * 60)

    print("\nHello! I'm CodeBot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.\n")

    conversation_count = 0

    while True:

        user_input = input("You: ")

        # Generate response
        response = chatbot_response(user_input)

        print(f"CodeBot: {response}\n")

        conversation_count += 1

        # Stop chatbot
        cleaned_input = clean_input(user_input)

        if cleaned_input in ["bye", "goodbye", "exit", "quit"]:
            print("-" * 60)
            print(f"Total messages exchanged: {conversation_count}")
            print("Thank you for using CodeBot!")
            print("-" * 60)
            break


# ------------------------------------------------------------
# Program entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()