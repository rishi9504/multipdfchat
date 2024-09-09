import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
 

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

def get_text_chunks(text):
    """
    Given a body of text, split it into 1000 character chunks
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.create_documents([text])
    return chunks

def get_vector_score(text_chunks):
    """
    Given a list of text chunks, create a vector store
    """
    

    embeddings = OpenAIEmbeddings() ## chargable, but using this
    # below is the way we can use for instruct embeddings on local systems with no money required

    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl") #too slow for current setup 
    vector_store = FAISS.from_documents(text_chunks, embeddings)

    return vector_store


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
                text_chunks = get_text_chunks(raw_text)


                # create vector store
                vector_store = get_vector_score(text_chunks)
        



if __name__ == "__main__":
    main()