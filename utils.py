# ============================================================
# CodeBot - Utility Functions
# ============================================================

import re
from difflib import SequenceMatcher


def clean_text(text):
    """
    Normalize user input.

    Steps:
    1. Convert text to lowercase.
    2. Remove punctuation.
    3. Remove extra spaces.
    """

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def similarity(text1, text2):
    """
    Calculate similarity between two strings.

    Returns a value between 0 and 1.
    """

    return SequenceMatcher(
        None,
        text1,
        text2
    ).ratio()


def contains_phrase(text, phrase):
    """
    Check whether a complete phrase exists in the text.
    """

    return phrase.lower() in text.lower()


def extract_name(message):
    """
    Try to extract a user's name from common sentences.

    Examples:

    My name is Sahil
    I am Sahil
    I'm Sahil
    Call me Sahil
    """

    patterns = [
        r"my name is ([a-zA-Z]+)",
        r"i am ([a-zA-Z]+)",
        r"im ([a-zA-Z]+)",
        r"call me ([a-zA-Z]+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, message, re.IGNORECASE)

        if match:
            return match.group(1).capitalize()

    return None