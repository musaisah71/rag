
import streamlit as st
import time
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain


# Set page configuration at the top level
st.set_page_config(page_title="Information retrieval")


def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("user: ", message.content)
        else:
            st.write("Reply: ", message.content)
        
        
        


def main():
    st.header("Musa's_AI_Chatbot")
    user_question = st.text_input("Ask a Question from the PDF Files")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)      



    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                time.sleep(2)
                st.success("Processing complete!")

# Ensure the main function is called correctly
if __name__ == "__main__":
    main()