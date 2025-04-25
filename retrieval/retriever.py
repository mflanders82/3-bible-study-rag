from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Step 1: Force local embedding model (avoids OpenAI fallback)
local_embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
Settings.embed_model = local_embed_model

# Step 2: Load the index from disk
storage_context = StorageContext.from_defaults(persist_dir="bible_index")
index = load_index_from_storage(storage_context)

# Step 3: Create a query engine and run the loop
query_engine = index.as_query_engine()

print("📖 Bible Study Retriever — Ask your question below (type 'exit' to quit):")
while True:
    query = input("\nAsk your Bible question: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye")
        break
    response = query_engine.query(query)
    print("\n🔎 Top Results:\n")
    print(response)
