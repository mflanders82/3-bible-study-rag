
# Bible Study AI - RAG Companion

This app helps you study scripture with AI-powered cross-referencing, commentary insights, and journaling.

## Structure
- `data/scripture`: Verse-by-verse text (start with KJV or ESV if allowed)
- `data/commentary`: Public domain commentaries (e.g., Matthew Henry)
- `data/lexicon`: Strong's concordance or other dictionaries
- `retrieval`: Embedding + search code (MiniLM + LlamaIndex)
- `journal-assistant`: Streamlit app and spiritual journaling tools

## Next Steps
1. Add scripture text into `data/scripture`
2. Add commentary (e.g., Henry's) to `data/commentary`
3. Run embedding pipeline in `retrieval/embedder.py`
4. Start Streamlit app from `journal-assistant/app.py`
