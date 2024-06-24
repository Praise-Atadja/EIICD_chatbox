import streamlit as st
from answer import answer_question

def main():
    st.title("Chat with AI: Ask Anything!")
    st.markdown("""
    Welcome to our AI-powered chatbox! Ask any question, and I'll do my best to provide you with an answer. Let's get started!
    """)

    input_text = st.text_area("Enter your question:", "")

    if st.button("Ask"):
        if input_text:
            answer = answer_question(input_text)
            st.success(f"Here's what I found: {answer}")
        else:
            st.warning("Oops! It seems like you forgot to ask a question. Please type your question in the box above.")

if __name__ == "__main__":
    main()
