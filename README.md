# 🤖 CodeBot — Rule-Based Chatbot

A beginner-friendly **Rule-Based Artificial Intelligence Chatbot** developed as part of the **CodeOrbit Tech Artificial Intelligence Internship**.

The chatbot uses predefined rules, keywords, and pattern matching to understand basic user inputs and provide appropriate responses.

---

## 📌 Internship Task

**Task 1: Rule-Based Chatbot**

### Requirements

* Build a simple chatbot using predefined rules or keywords.
* Handle common greetings.
* Answer basic questions.
* Provide a fallback response for unknown input.
* Use Python with basic `if-else` or pattern-matching logic.
* Add comments explaining how the chatbot determines its responses.

---

## 🎯 Objective

The objective of this project is to understand the basic concept of a **rule-based artificial intelligence system**.

Instead of using machine learning, the chatbot analyzes the user's input and compares it against predefined rules. When a matching rule is found, the chatbot returns the corresponding response.

---

## ✨ Features

* 👋 Greeting detection
* 🤖 Chatbot identity response
* 💬 Basic conversation
* 🆘 Help command
* 🕐 Current time response
* 🧠 Explanation of how the chatbot works
* 🙏 Thank-you response
* ❓ Fallback response for unknown questions
* 🚪 Exit commands
* 🧹 Input cleaning and normalization

---

## 🛠️ Technologies Used

* **Python**
* Regular Expressions (`re`)
* Python `datetime` module
* Conditional statements
* Keyword matching

No external libraries are required.

---

## 📂 Project Structure

```text
Rule-Based-Chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

---

## ⚙️ How the Chatbot Works

The chatbot follows a simple rule-based process:

```text
User Input
     ↓
Convert Input to Lowercase
     ↓
Remove Unnecessary Punctuation
     ↓
Check Predefined Rules
     ↓
Find Matching Keyword/Pattern
     ↓
Generate Appropriate Response
     ↓
Display Response
```

For example:

```python
if "how are you" in message:
    return "I'm doing great! Thanks for asking."
```

When the user enters a message containing `"how are you"`, the chatbot identifies the matching rule and returns the predefined response.

---

## 🧠 AI Logic

This chatbot is based on **rule-based artificial intelligence**.

It does not train on a dataset or use a machine learning model.

Instead, it uses predefined rules such as:

```text
hello → greeting response

your name → chatbot identity

how are you → status response

help → available commands

time → current time

thanks → thank-you response

bye → exit response
```

If none of the predefined rules match the user's input, the chatbot uses a fallback response.

Example:

```python
return (
    "I'm sorry, I don't understand that yet. "
    "Try asking something else or type 'help'."
)
```

This prevents the chatbot from remaining silent when it receives an unknown input.

---

## 🚀 Installation

### 1. Install Python

Make sure Python 3.9 or later is installed.

Check your Python version:

```bash
python --version
```

---

### 2. Clone or download the project

Place the project in your desired directory.

```text
Rule-Based-Chatbot/
```

---

### 3. Open the project folder

```bash
cd Rule-Based-Chatbot
```

---

### 4. Run the chatbot

```bash
python chatbot.py
```

---

## 💬 Example Conversation

```text
==================================================
        CODEBOT - RULE-BASED CHATBOT
==================================================
Type 'bye', 'exit', or 'quit' to end the chat.

You: hello
CodeBot: Hello! Nice to meet you. How can I help you?

You: what is your name
CodeBot: I am CodeBot, a simple rule-based AI chatbot.

You: how do you work
CodeBot: I use predefined rules and keywords. I analyze your
message and select a response that matches one of my rules.

You: what can you do
CodeBot: I can respond to greetings, answer simple questions,
tell you the time, and provide basic information about myself.

You: thanks
CodeBot: You're welcome! I'm happy to help.

You: bye
CodeBot: Goodbye! Have a great day!
```

---

## ❓ Fallback Response

If the chatbot receives an input that doesn't match any predefined rule, it responds with:

```text
I'm sorry, I don't understand that yet.
Try asking something else or type 'help'.
```

This is important because a chatbot should provide a response even when it cannot recognize the user's input.

---

## 🔍 Example Rules

| User Input         | Detected Rule | Chatbot Response             |
| ------------------ | ------------- | ---------------------------- |
| Hello              | Greeting      | Hello! Nice to meet you.     |
| What is your name? | Identity      | I am CodeBot.                |
| How are you?       | Status        | I'm doing great!             |
| What time is it?   | Time          | Displays current time        |
| Help               | Help          | Displays available features  |
| Thanks             | Appreciation  | You're welcome!              |
| Bye                | Exit          | Goodbye!                     |
| Unknown question   | Fallback      | I don't understand that yet. |

---

## 📚 Concepts Learned

Through this project, the following concepts were practiced:

* Python functions
* Conditional statements
* String processing
* Keyword matching
* Regular expressions
* Loops
* User input handling
* Exception-free fallback behavior
* Rule-based artificial intelligence

---

## 🔮 Future Improvements

The chatbot can be improved by adding:

* More conversation rules
* More natural language processing
* Sentiment analysis
* Machine learning
* Speech recognition
* Text-to-speech
* GUI interface
* Web interface using Streamlit
* Database-based responses
* Integration with an NLP model

---

## 👨‍💻 Internship Project

**Program:** Artificial Intelligence Internship
**Organization:** CodeOrbit Tech
**Task:** Task 1 — Rule-Based Chatbot
**Language:** Python


## 📄 License

This project was created for educational and internship purposes.
