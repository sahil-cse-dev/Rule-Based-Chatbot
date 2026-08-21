import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from chatbot_engine import CodeBot


class TestCodeBot(unittest.TestCase):

    def setUp(self):
        self.bot = CodeBot()

    def test_greeting(self):
        response = self.bot.respond("hello")

        self.assertTrue(response)

    def test_name_memory(self):
        self.bot.respond("my name is Sahil")

        response = self.bot.respond("what is my name")

        self.assertIn("Sahil", response)

    def test_python_intent(self):
        response = self.bot.respond(
            "tell me about python"
        )

        self.assertIn("Python", response)

    def test_machine_learning_intent(self):
        response = self.bot.respond(
            "what is machine learning"
        )

        self.assertIn(
            "Machine Learning",
            response
        )

    def test_ai_intent(self):
        response = self.bot.respond(
            "what is artificial intelligence"
        )

        self.assertIn(
            "Artificial Intelligence",
            response
        )

    def test_fuzzy_python(self):
        response = self.bot.respond("pythn")

        self.assertIn(
            "Python",
            response
        )

    def test_fallback(self):
        response = self.bot.respond(
            "explain quantum gravity"
        )

        self.assertTrue(
            "not confident" in response.lower()
            or "rephrase" in response.lower()
        )

    def test_help_command(self):
        response = self.bot.respond("/help")

        self.assertIn(
            "COMMANDS",
            response
        )

    def test_stats_command(self):
        response = self.bot.respond("stats")

        self.assertIn(
            "STATISTICS",
            response
        )

    def test_history_command(self):
        self.bot.respond("hello")

        response = self.bot.respond("history")

        self.assertIn(
            "HISTORY",
            response
        )


if __name__ == "__main__":
    unittest.main()