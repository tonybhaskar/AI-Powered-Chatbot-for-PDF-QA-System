from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

# Load raw data
def load_raw_data(input_dir):
    loader = SimpleDirectoryReader(input_dir=input_dir)
    return loader.load_data()

# Parse documents into nodes
def parse_documents(documents, chunk_size=128, chunk_overlap=16, paragraph_separator="\n\n"):
    parser = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        paragraph_separator=paragraph_separator
    )
    return parser.get_nodes_from_documents(documents, show_progress=True)
