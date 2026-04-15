# RAG Helpdesk Chatbot

## Overview

This project is a **Retrieval-Augmented Generation (RAG) based chatbot** designed to provide intelligent assistance for helpdesk queries. It is specifically tailored for handling issues related to the IMSS (Instituto Mexicano del Seguro Social) system, such as authentication errors, access problems, appointment closures, and other common system-related inquiries.

The chatbot leverages a pre-built knowledge base of documents, including markdown files, CSV data, and image placeholders (for future OCR integration), to deliver accurate, context-aware responses. It combines document retrieval with generative AI to ensure responses are grounded in the provided knowledge base.

## Key Features

- **RAG-Powered Responses**: Retrieves relevant information from a vectorized knowledge base and generates responses using a large language model (LLM).
- **Session-Based Memory**: Maintains conversation history per user session for coherent, multi-turn dialogues (up to 5 turns).
- **Streaming Responses**: Real-time streaming of AI-generated text for a smooth user experience.
- **Image Upload Support**: Allows users to upload images (e.g., error screenshots), which are base64-encoded and appended to the message (OCR integration planned for future releases).
- **Reset Functionality**: Users can reset chat memory for a fresh start.
- **Simple Web Widget**: Lightweight HTML-based frontend with a floating chat button, no heavy frameworks required.
- **Health Check Endpoint**: API endpoint for monitoring service status.
- **Modular Architecture**: Separates concerns into backend API, data processing, and frontend components.

## Architecture

The application follows a modular, microservice-like structure:

### Components

1. **Backend (app/)**:
   - `main.py`: FastAPI application entry point, configures CORS and includes API routes.
   - `api.py`: Defines RESTful endpoints (`/chat`, `/reset`, `/health`).
   - `chat_service.py`: Core logic for RAG pipeline, including context retrieval, prompt building, and LLM interaction.
   - `config.py`: Centralized configuration using environment variables.
   - `memory.py`: In-memory chat history management using LangChain message objects.
   - `frontend/widget.html`: Simple HTML/JavaScript widget for user interaction.

2. **Core Utilities (src/)**:
   - `file_processor.py`: Handles loading and chunking of various file types (Markdown, CSV, images).
   - `chroma_db.py`: Manages ChromaDB vector database creation and persistence.

3. **Data Layer (data/)**:
   - Knowledge base consisting of markdown documents, CSV files, and image files related to IMSS system issues (e.g., authentication errors, access problems).

4. **Vector Database (chroma/)**:
   - Persistent storage for document embeddings using ChromaDB.

### Data Flow

1. **Initialization**:
   - Documents from `data/` are loaded, chunked (1000 chars with 100 overlap), and embedded using HuggingFace models.
   - Embeddings are stored in ChromaDB for efficient similarity search.

2. **Query Processing**:
   - User message (text + optional image) is received via `/chat` endpoint.
   - Relevant documents are retrieved via similarity search (top-k results).
   - Context is combined with chat history and fed into a prompt template.
   - Groq LLM generates a streaming response, which is yielded back to the client.
   - Response is saved to session memory for future turns.

3. **Frontend Interaction**:
   - Users interact via the HTML widget, which sends requests to the FastAPI backend and displays streamed responses.

### Technologies Used

- **Programming Language**: Python 3.x
- **Web Framework**: FastAPI (for REST API with async support)
- **RAG Framework**: LangChain (for document processing, embeddings, and LLM chains)
- **Vector Database**: ChromaDB (for persistent vector storage and similarity search)
- **Embeddings**: HuggingFace Sentence Transformers (`all-MiniLM-L6-v2` by default)
- **LLM Provider**: Groq API (models like `llama-3.1-8b-instant`)
- **Text Processing**: Pandas (for CSV handling), LangChain Text Splitters (for chunking)
- **Frontend**: Vanilla HTML/CSS/JavaScript (no frameworks)
- **Environment Management**: python-dotenv (for configuration)
- **Other Libraries**: certifi (for SSL), base64 (for image encoding)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd rag_helpdesk
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     GROQ_MODEL=llama-3.1-8b-instant  # Optional, defaults to this
     EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2  # Optional
     TOP_K=3  # Number of docs to retrieve, optional
     CHROMA_DIR=chroma_db  # Vector DB path, optional
     MAX_CONTEXT_CHARS=4000  # Context limit, optional
     ```
   - Obtain a Groq API key from [Groq Console](https://console.groq.com/).

## Usage

1. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
   - The API will be available at `http://localhost:8000`.
   - On startup, the app processes the knowledge base and builds the vector database (this may take a moment on first run).

2. **Access the Chat Widget**:
   - Open `app/frontend/widget.html` in a web browser.
   - Click the floating chat button (💬) to open the widget.
   - Enter a session ID (auto-generated) or customize it.
   - Type a message or upload an image, then send.
   - Responses stream in real-time.

3. **API Endpoints**:
   - `POST /chat`: Send a message (with optional image). Returns streamed text response.
     - Body: Form data with `session_id`, `message`, `image` (file).
   - `POST /reset`: Reset chat memory for a session.
     - Body: JSON with `session_id`.
   - `GET /health`: Check service status.

## Notable Implementation Details

- **RAG Pipeline**: Uses LangChain's `RecursiveCharacterTextSplitter` for robust chunking. Similarity search retrieves top-k documents based on cosine similarity.
- **Memory Management**: Limited to 5 turns per session to prevent unbounded growth. Uses LangChain's `HumanMessage` and `AIMessage` for structured history.
- **Image Handling**: Currently placeholders images with descriptive text (e.g., "[Imagen detectada: error.png]"). Future versions could integrate OCR (e.g., Tesseract or Azure Vision).
- **Prompt Engineering**: System prompt enforces responses based only on provided context; fallback to "No hay información suficiente" if no relevant data.
- **Streaming**: Leverages FastAPI's `StreamingResponse` with `text/plain` for compatibility.
- **Data Sources**: Knowledge base includes merged markdown files, CSVs (e.g., access logs, studies), and images of common errors (e.g., invalid credentials, corrupted files).
- **Security**: CORS enabled for development; API key required for Groq. No authentication implemented yet.

## Future Enhancements

- Integrate OCR for image processing (e.g., extract text from error screenshots).
- Add user authentication and multi-user support.
- Expand knowledge base with more dynamic data sources.
- Implement persistent memory (e.g., using Redis or database).
- Add analytics/logging for chat interactions.
- Deploy to cloud (e.g., AWS, Vercel) with proper scaling.

## Contributing

Contributions are welcome! Please submit issues or pull requests for improvements.

## License

[Specify License, e.g., MIT]