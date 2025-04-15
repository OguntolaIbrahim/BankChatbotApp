import streamlit as st
from backend import get_response

def main():
    st.title("Bank Customer Service Chatbot")
    st.write("Welcome! How can I assist you today?")

    if 'history' not in st.session_state:
        st.session_state['history'] = []

    user_input = st.text_input("You:", "", key="user_input")

    if st.button("Send"):
        if user_input:
            response = get_response(user_input, st.session_state['history'])
            st.session_state['history'].append((user_input, response))

    for user_msg, bot_msg in st.session_state['history']:
        st.write(f"You: {user_msg}")
        st.write(f"Bot: {bot_msg}")

if __name__ == "__main__":
    main()