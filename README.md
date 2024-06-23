# PDF Chat Application

This project is a Streamlit-based application that allows users to chat with and ask questions about the content of uploaded PDF files. It uses Google's Generative AI for text embedding and question answering.

## Features

- Upload multiple PDF files
- Process and index PDF content
- Ask questions about the uploaded PDFs
- Get AI-generated answers based on the PDF content

## Components

The project consists of three main Python files:

1. `Main.py`: The main Streamlit application
2. `create_chunks.py`: Handles PDF text extraction and chunking
3. `Vector_store.py`: Manages vector embeddings and storage

## Requirements

- Streamlit
- PyPDF2
- LangChain
- Google Generative AI
- FAISS
- python-dotenv

## Setup

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run Main.py
   ```
2. Use the sidebar to upload PDF files
3. Click "Submit & Process" to index the PDFs
4. Ask questions in the main text input field
5. View AI-generated answers based on the PDF content

## How it works

1. PDFs are uploaded and processed into text chunks
2. Text chunks are embedded and stored in a FAISS index
3. User questions are embedded and compared to the stored vectors
4. Relevant text chunks are retrieved and used to generate an answer
5. The answer is displayed to the user
