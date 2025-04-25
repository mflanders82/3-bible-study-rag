from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from pathlib import Path

# Step 1: Load documents from the scripture folder
docs_path = Path("data/scripture")
documents = SimpleDirectoryReader(docs_path).load_data()

# Step 2: Define the embedding model (MiniLM)
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 3: Set up the service context
service_context = ServiceContext.from_defaults(embed_model=embed_model)

# Step 4: Create the vector store index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Step 5: Persist the index for later use
index.storage_context.persist("bible_index")

print("✅ Embeddings created and index saved to 'bible_index/'")
