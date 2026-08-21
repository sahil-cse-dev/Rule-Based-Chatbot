import streamlit as st
from chatbot_engine import CodeBot


st.set_page_config(
    page_title="CodeBot AI",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

if "bot" not in st.session_state:
    st.session_state.bot = CodeBot()

if "messages" not in st.session_state:
    st.session_state.messages = []


bot = st.session_state.bot


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🤖 CodeBot AI")

st.markdown(
    """
    **Advanced Rule-Based NLP Conversational System**

    A Python chatbot using predefined intents, fuzzy matching,
    entity extraction, conversation memory, and rule-based
    response selection.
    """
)

st.divider()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Chatbot Controls")

    st.write(
        "CodeBot uses rule-based NLP techniques to "
        "understand user messages."
    )

    st.subheader("Features")

    st.write("✅ Intent detection")
    st.write("✅ Fuzzy matching")
    st.write("✅ Entity extraction")
    st.write("✅ Conversation memory")
    st.write("✅ Knowledge base")
    st.write("✅ Chat history")
    st.write("✅ Statistics")
    st.write("✅ JSON logging")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.bot = CodeBot()
        st.session_state.messages = []

        st.rerun()


# ---------------------------------------------------------
# Chat History
# ---------------------------------------------------------

st.subheader("💬 Conversation")

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# ---------------------------------------------------------
# User Input
# ---------------------------------------------------------

user_input = st.chat_input(
    "Ask CodeBot something..."
)


if user_input:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Bot response
    response = bot.respond(
        user_input
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()


# ---------------------------------------------------------
# Example Questions
# ---------------------------------------------------------

if not st.session_state.messages:

    st.subheader("💡 Try asking")

    examples = [
        "What is Artificial Intelligence?",
        "What is Machine Learning?",
        "What is Python?",
        "How do you work?",
        "My name is Sahil",
        "What is my name?",
        "Tell me a joke"
    ]

    cols = st.columns(2)

    for index, example in enumerate(examples):

        with cols[index % 2]:

            if st.button(
                example,
                use_container_width=True
            ):

                st.session_state.messages.append(
                    {
                        "role": "user",
                        "content": example
                    }
                )

                response = bot.respond(
                    example
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

                st.rerun()