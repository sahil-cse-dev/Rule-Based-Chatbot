
class ConversationMemory:
    def __init__(self):
        self.name = None
        self.current_topic = None
        self.history = []
        self.message_count = 0

    def update_entities(self, entities):
        if "name" in entities:
            self.name = entities["name"]

    def add_turn(self, user, bot, intent, confidence):
        self.message_count += 1
        self.history.append({
            "user": user,
            "bot": bot,
            "intent": intent,
            "confidence": round(confidence, 3)
        })

    def clear(self):
        self.name = None
        self.current_topic = None
        self.history = []
        self.message_count = 0
