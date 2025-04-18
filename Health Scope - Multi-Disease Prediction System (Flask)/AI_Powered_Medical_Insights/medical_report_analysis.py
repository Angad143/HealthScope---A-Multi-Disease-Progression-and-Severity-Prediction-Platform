from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import re

# Initialize components
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

PROMPT_TEMPLATE = """
You are a medical report analysis assistant. Follow these rules strictly:
1. Answer ONLY using the provided medical report context
2. Keep responses very short (1-2 sentences maximum)
3. Use simple medical terms the patient would understand
4. If information isn't in the report, say: "Not found in the report"
5. Never guess or invent information
6. If user ask question which is not in report then say: "Not found in the report"

Context: {document_context}

Question: {user_query}

Answer (1-2 sentences, be exact):
"""

MEDICAL_KEYWORDS = [
    'patient', 'diagnosis', 'treatment', 'symptoms', 'medication', 
    'test results', 'blood pressure', 'heart rate', 'prescription',
    'allergies', 'history', 'clinical', 'doctor', 'nurse', 'hospital',
    'medical', 'report', 'findings', 'recommendations'
]

def is_medical_document(text):
    """Check if the document contains medical terminology"""
    text = text.lower()
    return any(keyword in text for keyword in MEDICAL_KEYWORDS)

def process_medical_report(file_path):
    try:
        # Load and process PDF
        loader = PDFPlumberLoader(file_path)
        documents = loader.load()
        
        # Check if document is medical
        combined_text = " ".join([doc.page_content for doc in documents])
        if not is_medical_document(combined_text):
            return {'error': 'Sorry, please upload a medical report as I am a medical report analysis system.'}
        
        # Split document into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunks = text_splitter.split_documents(documents)
        
        # Index documents
        DOCUMENT_VECTOR_DB.add_documents(chunks)
        
        return {'success': True}
    except Exception as e:
        return {'error': f'Error processing document: {str(e)}'}

def analyze_query(query):
    try:
        # Find relevant document sections
        relevant_docs = DOCUMENT_VECTOR_DB.similarity_search(query)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        
        # Generate response
        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        chain = prompt | LANGUAGE_MODEL
        response = chain.invoke({"user_query": query, "document_context": context})
        
        return {'response': response}
    except Exception as e:
        return {'error': f'Error analyzing query: {str(e)}'}