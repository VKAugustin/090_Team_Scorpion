# AI_Challange_2024
It is a AI bot intergrated webpage to Know details about 2024 election candidates

# Presidential Election 2024 Chatbot

## Overview

This project is a web application that provides information about all candidates for the 2024 presidential election. It allows users to interact with an AI chatbot to obtain details about each candidate, including their election symbol, promises, and other relevant information. Additionally, the chatbot can fetch recent news articles related to the candidates or election topics using the GNews API.

## Features

- **AI Chatbot:** Interact with an AI chatbot that answers questions based on the content of multiple PDFs containing detailed information about each candidate.
- **Multi-PDF Support:** Load and process multiple PDFs containing candidate information.
- **News Search:** Fetch and display relevant news articles using the GNews API.
- **Web Interface:** User-friendly web interface to interact with the chatbot.

## Prerequisites

- Python 3.8 or higher
- Flask
- langchain_community
- langchain_groq
- requests
- dotenv

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/VKAugustin/AI_Challange_2024.git
   cd presidential-election-chatbot

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt

4. **Set Up Environment Variables**

    ```bash
    GNEWS_API_KEY=your_gnews_api_key
    GROQ_API_KEY=your_groq_api_key

5. **Add PDF Files**

    Place all your PDF files containing candidate information in the "pdf_files" directory.


*How It Works*

    Document Loading:
        The application loads multiple PDFs from the pdf_files directory.
        Each PDF is processed to extract text and split into chunks.

    Vector Store:
        The text chunks from all PDFs are indexed using the FAISS vector store for efficient retrieval.

    Chatbot Interaction:
        The AI chatbot uses the ChatGroq model to generate responses based on the indexed documents.
        For news-related queries, the application fetches recent news articles using the GNews API.

Project Structure

    app.py: Main application script.
    requirements.txt: List of dependencies.
    .env: Environment variables configuration.
    pdf_files/: Directory containing PDF files with candidate information.
    templates/: Directory containing HTML templates.

Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

    LangChain
    HuggingFace Embeddings
    GNews API

