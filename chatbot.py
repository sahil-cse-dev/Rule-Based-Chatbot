
from chatbot_engine import CodeBot

def main():
    bot = CodeBot()
    print("=" * 70)
    print("                 🤖 CODEBOT ADVANCED")
    print("       Rule-Based NLP Conversational System")
    print("=" * 70)
    print("Commands: /help  /history  /stats  /clear  /export  /quit")
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nCodeBot: Goodbye! 👋")
            break

        if not user_input:
            print("CodeBot: Please enter a message.\n")
            continue

        if user_input.lower() in {"/quit", "quit", "exit", "bye", "goodbye"}:
            print("CodeBot: Goodbye! Keep learning and coding. 🚀")
            break

        response = bot.respond(user_input)
        print(f"CodeBot: {response}\n")

if __name__ == "__main__":
    main()
