# ============================================================
# CodeBot - Intent Definitions
# CodeOrbit Tech AI Internship
# Task 1: Advanced Rule-Based Chatbot
# ============================================================

# Each intent contains:
# - keywords: words that help identify the user's intention
# - responses: possible responses for that intent

INTENTS = {

    "greeting": {
        "keywords": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ],
        "responses": [
            "Hello! 👋 How can I help you today?",
            "Hi there! I'm CodeBot. What would you like to know?",
            "Hey! Nice to meet you. 😊"
        ]
    },

    "goodbye": {
        "keywords": [
            "bye",
            "goodbye",
            "see you",
            "exit",
            "quit"
        ],
        "responses": [
            "Goodbye! 👋 Have a great day!",
            "See you later! Thanks for chatting with CodeBot.",
            "Goodbye! Keep learning and coding. 🚀"
        ]
    },

    "bot_identity": {
        "keywords": [
            "your name",
            "who are you",
            "what are you",
            "tell me about yourself"
        ],
        "responses": [
            "I'm CodeBot, a rule-based AI chatbot built using Python.",
            "My name is CodeBot. I use predefined rules and NLP-style text processing to respond to users."
        ]
    },

    "bot_status": {
        "keywords": [
            "how are you",
            "how r you",
            "are you okay",
            "how are things"
        ],
        "responses": [
            "I'm doing great! Thanks for asking. 😊",
            "I'm functioning perfectly and ready to chat!",
            "All systems are running smoothly! 🤖"
        ]
    },

    "ai": {
        "keywords": [
            "what is ai",
            "artificial intelligence",
            "define ai"
        ],
        "responses": [
            "Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks requiring human-like intelligence."
        ]
    },

    "machine_learning": {
        "keywords": [
            "machine learning",
            "what is ml",
            "what is machine learning"
        ],
        "responses": [
            "Machine Learning is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions."
        ]
    },

    "python": {
        "keywords": [
            "python",
            "what is python",
            "python language"
        ],
        "responses": [
            "Python is a high-level programming language known for its simple syntax. It is widely used in AI, machine learning, web development, automation, and data science."
        ]
    },

    "programming": {
        "keywords": [
            "programming",
            "coding",
            "write code",
            "programming language"
        ],
        "responses": [
            "Programming is the process of creating instructions that tell a computer how to perform specific tasks."
        ]
    },

    "internship": {
        "keywords": [
            "internship",
            "codeorbit",
            "internship task",
            "ai internship"
        ],
        "responses": [
            "This chatbot was developed as Task 1 of the CodeOrbit Tech Artificial Intelligence Internship."
        ]
    },

    "capabilities": {
        "keywords": [
            "what can you do",
            "your features",
            "features",
            "capabilities"
        ],
        "responses": [
            "I can answer basic AI and programming questions, detect greetings, respond to sentiment, tell you the date and time, remember your name, and handle common conversation commands."
        ]
    },

    "how_it_works": {
        "keywords": [
            "how do you work",
            "how you work",
            "how were you made",
            "how are you made"
        ],
        "responses": [
            "I process your text, normalize it, detect keywords and patterns, identify an intent, and then select a predefined response."
        ]
    },

    "thanks": {
        "keywords": [
            "thank you",
            "thanks",
            "thank"
        ],
        "responses": [
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime! 🚀"
        ]
    },

    "joke": {
        "keywords": [
            "joke",
            "make me laugh",
            "funny"
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why was the computer cold? It left its Windows open! 😂"
        ]
    },

    "positive": {
        "keywords": [
            "good",
            "great",
            "awesome",
            "excellent",
            "amazing",
            "nice"
        ],
        "responses": [
            "That's great to hear! 😄",
            "Awesome! Keep that positive energy going! 🚀"
        ]
    },

    "negative": {
        "keywords": [
            "sad",
            "bad",
            "upset",
            "angry",
            "terrible",
            "depressed"
        ],
        "responses": [
            "I'm sorry you're feeling that way. I hope things get better soon.",
            "That doesn't sound good. Take a little time for yourself and keep going."
        ]
    }
}