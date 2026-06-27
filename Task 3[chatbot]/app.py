import streamlit as st
from chatbot import chatbot_response

st.set_page_config(
    page_title="Intellex",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Intellex")
st.caption("Your intelligent rule-based chatbot assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
Hello! I am Intellex.

I can help you with:
1. Simple questions  
2. Wikipedia-based general knowledge  
3. Maths calculations like 45*2  
4. Study and exam guidance  
5. Motivation  
6. Jokes  
7. Date and time  
8. CODSOFT project doubts  

Type anything normally.
"""
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask Intellex anything...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = chatbot_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()