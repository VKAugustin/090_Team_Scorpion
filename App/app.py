from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
import requests  

load_dotenv()

app = Flask(__name__)

# Directory where the PDFs are stored
pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf_files")


def search_news(query):
    api_key = os.getenv("GNEWS_API_KEY")
    url = f"https://gnews.io/api/v4/search?q={query}&token={api_key}&lang=en"
    response = requests.get(url)
    data = response.json()
    if "articles" in data and data["articles"]:
        top_article = data["articles"][0]
        return f"Here's a news article I found: {top_article['url']} - {top_article['title']}"
    return "Sorry, I couldn't find relevant news articles."


def load_documents(pdf_dir):
    all_documents = []
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            file_path = os.path.join(pdf_dir, pdf_file)
            loader = UnstructuredPDFLoader(file_path)
            documents = loader.load()
            all_documents.extend(documents)
    return all_documents


def setup_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings()
    text_splitter = CharacterTextSplitter(
        separator="\n",  
        chunk_size=1000,
        chunk_overlap=200
    )
    doc_chunks = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(doc_chunks, embeddings)
    return vectorstore


def create_chain(vectorstore):
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0
    )
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="map_reduce",
        memory=memory,
        verbose=True
    )
    return chain

def handle_greetings(message):
    greetings = ["hi", "hello", "hey", "greetings", "howdy"]
    if any(greeting in message.lower() for greeting in greetings):
        return "Hi! this is Scorpion Bot 🦂, How can I help you today?"
    return None

def check_relevance(response):
    if len(response) < 20 or "I don't know" in response:
        return False
    return True


documents = load_documents(pdf_dir)
vectorstore = setup_vectorstore(documents)
conversation_chain = create_chain(vectorstore)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["message"]
    
   
    greeting_response = handle_greetings(user_input)
    if greeting_response:
        return jsonify({"response": greeting_response})
    
  
    if "news" in user_input.lower():
        news_response = search_news(user_input)
        return jsonify({"response": news_response})
    
    
    response = conversation_chain({"question": user_input})
    assistant_response = response["answer"]
    
    
    if not check_relevance(assistant_response):
        assistant_response = ("It seems like I couldn't find relevant information on that topic. "
                              "You might want to ask about the content of the document or something related to the 2024 election.")
    
    return jsonify({"response": assistant_response})

if __name__ == "__main__":
    app.run(debug=True)
