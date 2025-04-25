from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from pathlib import Path

# Step 1: Load documents
docs_path = Path("/Users/ironcloth/Documents/3-bible-study-rag/retrieval/data/scripture")
documents = SimpleDirectoryReader(docs_path).load_data()

# Step 2: Explicitly load a local embedding model
local_embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 3: Set this local model in the Settings explicitly
Settings.embed_model = local_embed_model

# Step 4: Build the index
index = VectorStoreIndex.from_documents(documents)

# Step 5: Persist the index to disk
index.storage_context.persist(persist_dir="bible_index")

print("✅ Embeddings created with local model. Index saved to 'bible_index/'")
