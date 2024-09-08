import streamlit as st
from dotenv import load_dotenv
from pypdf2 import PdfReader


def get_pdf_text(pdf_docs):
    """
    Given a list of pdf file paths, read all the text out of the documents
    and return it as a single string.

    Parameters
    ----------
    pdf_docs : list of str
        A list of paths to pdf files

    Returns
    -------
    str
        The text from all the pdfs, concatenated
    """
    text = ""

    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text





def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide")
    st.header("Chat with multiple PDFs")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your documents", accept_multiple_files=True, type=["pdf"])
        if st.button("Process"):
            with st.spinner("Processing your documents..."):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)


                # get the text chunks

                # create vector store
        



if __name__ == "__main__":
    main()