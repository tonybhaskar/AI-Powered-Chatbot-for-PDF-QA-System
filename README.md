
# GenAI Project: AI-Powered Chatbot for PDF QA System 

This project implements an AI-powered chatbot with contextual memory using Flask, the LlamaIndex library, and ChromaDB for document storage. The chatbot is powered by a large language model (LLM) from Ollama and provides contextual responses based on documents stored in a ChromaDB collection.

## Features

- **Data Loading and Indexing**: Upload documents, extract embeddings, and store them in ChromaDB.
- **Query Endpoint**: Submit a query to the AI model, which retrieves relevant documents and generates a context-aware response.
- **Flask API**: A simple RESTful API built with Flask to interact with the chatbot.

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python 3.7+**
- **Ollama** (for Llama-based large language models)
- **ChromaDB** (for document storage)
- **Flask** (for building the API)

### Python Libraries

Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Setup Instructions

1. **Create a Virtual Environment**: 

   To set up a virtual environment, run the following command:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:

   Once the virtual environment is activated, install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:
   
   To start the Flask app, run:

   ```bash
   python run.py
   ```

   The app will start on `http://127.0.0.1:5000/`.

5. **Test the API**:
   Use **Postman** or **curl** to test the API.

   - **Load Data**:
     Endpoint: `/load-data` (POST)

     This endpoint uploads the documents and stores the embeddings in ChromaDB.

     Example:
     ```bash
     curl -X POST http://127.0.0.1:5000/load-data
     ```

   - **Query the AI Model**:
     Endpoint: `/query` (POST)

     Submit a query and get a response based on the indexed documents.

     Example:
     ```bash
     curl -X POST http://127.0.0.1:5000/query        -H "Content-Type: application/json"        -d '{"query": "What are transformers?"}'
     ```

     The response will include:
     ```json
     {
         "query": "What are transformers?",
         "response": "Transformers are ... (generated response)",
         "documents": [
             "Relevant document content 1",
             "Relevant document content 2"
         ]
     }
     ```

## Endpoint Details

### `/load-data` (POST)

- **Purpose**: Loads raw data, parses documents, extracts embeddings, and stores them in ChromaDB.
- **Response**:
  - Success: `{ "message": "Data loaded and indexed successfully.", "documents_count": <count> }`
  - Error: An error message in case of failure.

### `/query` (POST)

- **Purpose**: Accepts a query and returns the generated response along with the relevant documents.
- **Request Body**:
  - `query`: The text query string to ask the AI model.
  
- **Response**:
  - `query`: The original query.
  - `response`: The model-generated response.
  - `documents`: The top 5 relevant documents based on the query.

## Contributing

Feel free to fork this project and submit pull requests. If you find any issues or have suggestions, please open an issue.

## License

This project is licensed under the MIT License.

---

Enjoy exploring and building with AI!
