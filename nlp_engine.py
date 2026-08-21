import re
from difflib import SequenceMatcher


STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "am",
    "i",
    "me",
    "my",
    "to",
    "of",
    "for",
    "in",
    "on",
    "what",
    "who",
    "how",
    "can",
    "you",
    "do",
    "tell",
    "about",
    "please",
    "it",
    "this",
    "that",
    "does",
    "does"
}


def preprocess(text):
    """
    Normalize user input.

    Converts text to lowercase, removes punctuation,
    and removes unnecessary whitespace.
    """

    text = text.lower()

    text = re.sub(
        r"[^\w\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def tokens(text):
    """
    Return meaningful tokens after removing common
    stopwords.
    """

    return [
        token
        for token in preprocess(text).split()
        if token not in STOPWORDS
    ]


def similarity(a, b):
    """
    Calculate fuzzy similarity between two strings.

    Returns a value between 0 and 1.
    """

    return SequenceMatcher(
        None,
        a,
        b
    ).ratio()


def score_intents(text, intents):
    """
    Score every intent using:

    1. Exact phrase matching
    2. Phrase containment
    3. Token overlap
    4. Conservative fuzzy matching

    The scoring deliberately avoids allowing a common word
    such as 'explain' to produce a high-confidence match.
    """

    clean = preprocess(text)

    user_tokens = set(tokens(clean))

    results = []

    for intent_name, data in intents.items():

        best_score = 0.0

        for pattern in data.get(
            "patterns",
            []
        ):

            clean_pattern = preprocess(
                pattern
            )

            pattern_tokens = set(
                tokens(clean_pattern)
            )

            # ==================================================
            # 1. Exact match
            # ==================================================

            if clean == clean_pattern:

                score = 1.0

            # ==================================================
            # 2. Exact phrase contained in the input
            #
            # Only allow this when the phrase contains at least
            # one meaningful token and the matched phrase is
            # substantial.
            # ==================================================

            elif (
                len(pattern_tokens) >= 2
                and clean_pattern in clean
            ):

                score = 0.95

            # ==================================================
            # 3. Token overlap
            # ==================================================

            elif pattern_tokens:

                overlap_count = len(
                    user_tokens & pattern_tokens
                )

                overlap_ratio = (
                    overlap_count
                    / len(pattern_tokens)
                )

                # No meaningful shared words = no match.
                if overlap_count == 0:

                    score = 0.0

                # A single generic word such as "explain",
                # "tell", or "what" should not identify an intent.
                elif (
                    overlap_count == 1
                    and len(user_tokens) >= 2
                ):

                    score = min(
                        0.25,
                        0.80 * overlap_ratio
                    )

                else:

                    score = (
                        0.80
                        * overlap_ratio
                    )

            else:

                score = 0.0

            # ==================================================
            # 4. Conservative fuzzy matching
            #
            # Only use fuzzy matching for short inputs,
            # especially spelling mistakes such as:
            #
            #     pythn -> python
            #
            # We do NOT fuzzy-match long sentences because
            # generic words can create false positives.
            # ==================================================

            if (
                len(clean.split()) <= 2
                and len(clean_pattern.split()) <= 3
            ):

                fuzzy = similarity(
                    clean,
                    clean_pattern
                )

                if fuzzy >= 0.82:

                    score = max(
                        score,
                        0.75 * fuzzy
                    )

            best_score = max(
                best_score,
                score
            )

        results.append(
            (
                intent_name,
                round(best_score, 3)
            )
        )

    return sorted(
        results,
        key=lambda item: item[1],
        reverse=True
    )


def extract_entities(text):
    """
    Extract simple entities such as:

    - person's name
    - technology
    """

    entities = {}

    name_patterns = [
        (
            r"\bmy name is ([A-Za-z][A-Za-z'-]{1,30})",
            "name"
        ),
        (
            r"\bi am ([A-Za-z][A-Za-z'-]{1,30})",
            "name"
        ),
        (
            r"\bi'm ([A-Za-z][A-Za-z'-]{1,30})",
            "name"
        ),
        (
            r"\bcall me ([A-Za-z][A-Za-z'-]{1,30})",
            "name"
        )
    ]

    for pattern, entity_type in name_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            entities[entity_type] = (
                match.group(1).capitalize()
            )

            break

    technologies = [
        "python",
        "java",
        "c++",
        "javascript",
        "machine learning",
        "artificial intelligence"
    ]

    lower_text = text.lower()

    for technology in technologies:

        if technology in lower_text:

            entities[
                "technology"
            ] = technology

    return entities