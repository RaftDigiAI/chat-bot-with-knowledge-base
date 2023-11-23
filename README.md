# A Retail Chatbot for perfume suggestions

# Running bot
1. Create virtual environment
2. Copy .env.template to .env and fill in the values OPEN_AI_LLM_MODEL and OPENAI_API_KEY
3. Install requirements `pip install -r requirements.txt`
4. Install and start weaviate database. See https://weaviate.io/developers/weaviate/installation for instructions. You can setup either a local instance or a cloud instance (https://console.weaviate.cloud/). Cloud is free for 21 day.
5. Update WEVIATE_URL in .env to point to the weaviate instance
6. Run `streamlit run chat.py` to start the app in the browser

# Creating vector database
1. Create virtual environment
2. Copy .env.template to .env and fill in the values OPEN_AI_LLM_MODEL and OPENAI_API_KEY
2. Install requirements `pip install -r requirements.txt`
3. Run `python build_vector_database.py` to create the vector database