import json
import random
from datetime import datetime
from pathlib import Path

from nlp_engine import preprocess, score_intents, extract_entities
from memory import ConversationMemory


# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

INTENTS_FILE = BASE_DIR / "intents" / "intents.json"
KNOWLEDGE_FILE = BASE_DIR / "knowledge" / "knowledge.json"
LOG_DIR = BASE_DIR / "logs"


# ============================================================
# CodeBot
# ============================================================

class CodeBot:

    def __init__(self):

        # Load intent configuration
        self.intents = json.loads(
            INTENTS_FILE.read_text(
                encoding="utf-8"
            )
        )

        # Load knowledge base
        self.knowledge = json.loads(
            KNOWLEDGE_FILE.read_text(
                encoding="utf-8"
            )
        )

        # Conversation memory
        self.memory = ConversationMemory()

        # Create log directory
        LOG_DIR.mkdir(
            exist_ok=True
        )

    # ========================================================
    # Save Conversation Log
    # ========================================================

    def _save_log(
        self,
        user_text,
        intent,
        confidence,
        response,
        entities
    ):

        log_file = LOG_DIR / (
            f"conversations_"
            f"{datetime.now():%Y-%m-%d}.jsonl"
        )

        record = {

            "timestamp":
                datetime.now().isoformat(
                    timespec="seconds"
                ),

            "user":
                user_text,

            "intent":
                intent,

            "confidence":
                round(confidence, 3),

            "entities":
                entities,

            "response":
                response
        }

        with log_file.open(
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                )
                + "\n"
            )

    # ========================================================
    # Help
    # ========================================================

    def _help(self):

        return (
            "\n"
            "========== CODEBOT COMMANDS ==========\n"
            "/help      Show commands\n"
            "/history   Show recent conversation\n"
            "/stats     Show chatbot statistics\n"
            "/clear     Clear conversation memory\n"
            "/export    Export current conversation\n"
            "/quit      Exit chatbot\n"
            "====================================="
        )

    # ========================================================
    # Statistics
    # ========================================================

    def _stats(self):

        return (
            "\n"
            "========== STATISTICS ==========\n"
            f"Messages: {self.memory.message_count}\n"
            f"Known intents: {len(self.intents)}\n"
            f"User name: {self.memory.name or 'Unknown'}\n"
            f"Current topic: "
            f"{self.memory.current_topic or 'None'}\n"
            f"Stored history items: "
            f"{len(self.memory.history)}\n"
            "================================"
        )

    # ========================================================
    # Conversation History
    # ========================================================

    def _history(self):

        if not self.memory.history:

            return (
                "CodeBot: "
                "No conversation history yet."
            )

        lines = [
            "",
            "========== RECENT HISTORY =========="
        ]

        for item in self.memory.history[-10:]:

            lines.append(
                f"You: {item['user']}"
            )

            lines.append(
                f"Bot: {item['bot']}"
            )

        lines.append(
            "===================================="
        )

        return "\n".join(lines)

    # ========================================================
    # Export Conversation
    # ========================================================

    def _export(self):

        export_dir = BASE_DIR / "logs"

        export_dir.mkdir(
            exist_ok=True
        )

        path = export_dir / (
            f"conversation_export_"
            f"{datetime.now():%Y%m%d_%H%M%S}.json"
        )

        path.write_text(
            json.dumps(
                self.memory.history,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

        return (
            "Conversation exported to "
            f"{path.relative_to(BASE_DIR)}"
        )

    # ========================================================
    # Knowledge Base Response
    # ========================================================

    def _knowledge_response(self, topic):

        data = self.knowledge.get(topic)

        if not data:

            return None

        definition = data.get(
            "definition",
            ""
        )

        extra = data.get(
            "extra",
            ""
        )

        return (
            f"{definition} {extra}"
        ).strip()

    # ========================================================
    # Command Handler
    # ========================================================

    def _handle_command(self, text):

        # Help
        if text in {
            "/help",
            "help"
        }:

            return self._help()

        # History
        if text in {
            "/history",
            "history"
        }:

            return self._history()

        # Statistics
        if text in {
            "/stats",
            "stats"
        }:

            return self._stats()

        # Clear memory
        if text in {
            "/clear",
            "clear"
        }:

            self.memory.clear()

            return (
                "Conversation memory "
                "has been cleared. 🧹"
            )

        # Export
        if text in {
            "/export",
            "export"
        }:

            return self._export()

        # No command detected
        return None

    # ========================================================
    # Main Response Engine
    # ========================================================

    def respond(self, user_text):

        # ----------------------------------------------------
        # Normalize input
        # ----------------------------------------------------

        text = preprocess(
            user_text
        )

        # ----------------------------------------------------
        # Command handling
        # ----------------------------------------------------

        command_response = (
            self._handle_command(text)
        )

        if command_response:

            return command_response

        # ----------------------------------------------------
        # Entity extraction
        # ----------------------------------------------------

        entities = extract_entities(
            user_text
        )

        self.memory.update_entities(
            entities
        )

        # ----------------------------------------------------
        # Intent scoring
        # ----------------------------------------------------

        scores = score_intents(
            text,
            self.intents
        )

        if scores:

            intent, confidence = scores[0]

        else:

            intent = None
            confidence = 0.0

        # ----------------------------------------------------
        # Context carry-over
        # ----------------------------------------------------

        if (
            len(text.split()) <= 6
            and self.memory.current_topic
        ):

            context_intent = self.intents.get(
                self.memory.current_topic
            )

            context_words = {
                "creator",
                "created",
                "uses",
                "use",
                "why",
                "example",
                "definition"
            }

            if (
                context_intent
                and any(
                    word in text.split()
                    for word in context_words
                )
            ):

                intent = (
                    self.memory.current_topic
                )

                confidence = max(
                    confidence,
                    0.80
                )

        # ----------------------------------------------------
        # Low confidence fallback
        # ----------------------------------------------------

        if (
            confidence < 0.45
            or intent is None
        ):

            response = (
                "I'm not confident I understood that. 🤔\n"
                "Could you rephrase it?\n"
                "Type 'help' to see what I can do."
            )

            self.memory.add_turn(
                user_text,
                response,
                intent,
                confidence
            )

            self._save_log(
                user_text,
                intent,
                confidence,
                response,
                entities
            )

            return response

        # ----------------------------------------------------
        # Update current topic
        # ----------------------------------------------------

        self.memory.current_topic = intent

        # ====================================================
        # Response Generation
        # ====================================================

        # ----------------------------------------------------
        # Greeting
        # ----------------------------------------------------

        if intent == "greeting":

            name = self.memory.name

            if name:

                response = (
                    f"Hello {name}! 👋 "
                    "How can I help you?"
                )

            else:

                response = random.choice(
                    self.intents[
                        intent
                    ]["responses"]
                )

        # ----------------------------------------------------
        # Name Query
        # ----------------------------------------------------

        elif intent == "name_query":

            if self.memory.name:

                response = (
                    f"Your name is "
                    f"{self.memory.name}. 😊"
                )

            else:

                response = (
                    "You haven't told me your "
                    "name yet.\n"
                    "Try saying: My name is Sahil."
                )

        # ----------------------------------------------------
        # Time
        # ----------------------------------------------------

        elif intent == "time":

            response = (
                "The current time is "
                f"{datetime.now():%I:%M %p}. 🕐"
            )

        # ----------------------------------------------------
        # Date
        # ----------------------------------------------------

        elif intent == "date":

            response = (
                "Today's date is "
                f"{datetime.now():%d %B %Y}. 📅"
            )

        # ----------------------------------------------------
        # Python
        # ----------------------------------------------------

        elif intent == "python":

            response = (
                self._knowledge_response(
                    "python"
                )
                or random.choice(
                    self.intents[
                        intent
                    ]["responses"]
                )
            )

        # ----------------------------------------------------
        # Artificial Intelligence
        # ----------------------------------------------------

        elif intent == "artificial_intelligence":

            response = (
                self._knowledge_response(
                    "artificial_intelligence"
                )
                or random.choice(
                    self.intents[
                        intent
                    ]["responses"]
                )
            )

        # ----------------------------------------------------
        # Machine Learning
        # ----------------------------------------------------

        elif intent == "machine_learning":

            response = (
                self._knowledge_response(
                    "machine_learning"
                )
                or random.choice(
                    self.intents[
                        intent
                    ]["responses"]
                )
            )

        # ----------------------------------------------------
        # All Other Intents
        # ----------------------------------------------------

        else:

            responses = self.intents[
                intent
            ].get(
                "responses",
                []
            )

            if responses:

                response = random.choice(
                    responses
                )

            else:

                response = (
                    "I detected the "
                    f"'{intent}' intent, "
                    "but I don't have a response "
                    "configured for it yet."
                )

        # ----------------------------------------------------
        # Save Conversation
        # ----------------------------------------------------

        self.memory.add_turn(
            user_text,
            response,
            intent,
            confidence
        )

        self._save_log(
            user_text,
            intent,
            confidence,
            response,
            entities
        )

        return response