from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.tools import tool


loader = PyPDFLoader(
    "/home/pradeep/Downloads/Durga_Data_analyst.pdf"
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)



embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./vector_db"
)

@tool
def find_vector(user_query: str):
    """
    Search the candidate's resume.

    Use this tool whenever you need information about the candidate's
    name, profile, experience, internships, projects, education,
    technical skills, certifications, achievements, responsibilities,
    technologies, tools, or any other resume-specific information.

    Pass a specific search query describing exactly what information
    you need from the resume.
    """

    results = vector_store.similarity_search(
        user_query,
        k=4
    )
    
    context = "\n\n".join(
        doc.page_content for doc in results
    )
    print(f'query= {user_query} ,  context = {context}')
    return context
