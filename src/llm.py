



from llama_index.llms.ollama import Ollama

def get_llm():
    """
    Initializes the LLM (Large Language Model) for querying.
    
    Returns:
        Ollama: The LLM instance.
    """
    llm = Ollama(model="llama3.2:1b", base_url="http://localhost:11434", request_timeout=120.0)
    return llm

def get_embedding_client():
    """
    Initialize and return the embedding client.
    
    Returns:
        OllamaEmbedding: The embedding client instance.
    """
    from llama_index.embeddings.ollama import OllamaEmbedding
    ollama_embedding = OllamaEmbedding(
        model_name="all-minilm:latest",
        base_url="http://localhost:11434",
        ollama_additional_kwargs={"mirostat": 0}
    )
    return ollama_embedding

def generate_response(llm, documents, query):
    """
    Generate a response based on the query and relevant documents.
    
    Args:
        llm: The language model instance.
        documents: List of relevant documents.
        query: The query string.

    Returns:
        str: The generated response text.
    """
    # Combine the documents into a context
    context = " ".join(documents[0]) + " " + query

    # Get the completion response from the LLM
    completion_response = llm.complete(prompt=context)

    # Check if the response is JSON serializable, specifically extract the text from the response
    if hasattr(completion_response, 'text'):  # Check if `text` attribute exists
        response_text = completion_response.text
    else:
        # Fallback in case the structure is unexpected
        raise ValueError("LLM response does not contain a 'text' attribute")

    return response_text
