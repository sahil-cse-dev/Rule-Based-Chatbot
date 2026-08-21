# 🤖 CodeBot — Advanced Rule-Based NLP Chatbot

A modular, beginner-friendly but advanced **rule-based NLP chatbot** created for **CodeOrbit Tech — Artificial Intelligence Internship, Task 1**.

## Features

- Intent detection with confidence scoring
- Keyword, phrase, overlap, and fuzzy matching
- Text normalization
- Entity extraction for names and technologies
- Conversation memory
- Context-aware short follow-up handling
- JSON-based intent configuration
- JSON knowledge base
- Conversation logging
- Chat history
- Conversation statistics
- Exportable conversation history
- CLI commands
- Fallback and clarification response
- Automated unit tests
- No external API or paid AI service

## Architecture

```text
User
 ↓
Preprocessing
 ↓
Intent Scoring
 ├── Phrase Matching
 ├── Token Overlap
 └── Fuzzy Similarity
 ↓
Intent + Confidence
 ↓
Entity Extraction
 ↓
Conversation Memory
 ↓
Response Engine
 ↓
User
```

## Project Structure

```text
Rule-Based-Chatbot/
├── chatbot.py
├── chatbot_engine.py
├── nlp_engine.py
├── memory.py
├── intents/
│   └── intents.json
├── knowledge/
│   └── knowledge.json
├── logs/
├── tests/
│   └── test_chatbot.py
├── screenshots/
├── README.md
└── requirements.txt
```

## Run

```bash
python chatbot.py
```

## Commands

```text
/help
/history
/stats
/clear
/export
/quit
```

## Example

```text
You: my name is Sahil
CodeBot: Nice to meet you, Sahil! 😊 I'll remember your name during this conversation.

You: what is python?
CodeBot: Python is a high-level, general-purpose programming language...

You: what is my name?
CodeBot: Your name is Sahil. 😊

You: stats
CodeBot: Messages: 3
```

## AI / NLP Concepts

This project demonstrates rule-based NLP concepts rather than machine learning. The system compares user input against predefined patterns and calculates a confidence score. Entity extraction and conversation memory provide additional context.

## Internship Alignment

This project satisfies CodeOrbit Task 1 requirements:

- Python implementation
- Predefined rules and keywords
- Greeting handling
- Question handling
- Fallback response
- Comments and modular explanation
- Beginner-friendly implementation

## Future Improvements

- Streamlit web interface
- Multilingual rules
- Voice input/output
- More advanced entity extraction
- Database-backed knowledge
- ML-based intent classifier as a separate experiment
