from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

def vectorstore(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vectors = FAISS.from_texts(chunks,embedding=embeddings)
    vectors.save_local("Faiss.index")