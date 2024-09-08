import streamlit as st




def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide")
    st.header("Chat with multiple PDFs")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your documents", accept_multiple_files=True, type=["pdf"])
        st.button("Process")
        



if __name__ == "__main__":
    main()