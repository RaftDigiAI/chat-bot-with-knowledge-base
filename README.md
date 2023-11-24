# A Retail Chatbot for perfume suggestions

# Technologies
- Python
- Streamlit - for the UI
- Weaviate - for the knowledge vector search
- OpenAI - for the language model
- Langchain - for building AI pipeline

# Prerequisites
1. Open AI Api account. See https://platform.openai.com/overview for instructions
2. Weaviate instance. See https://weaviate.io/developers/weaviate/installation for instructions. You can setup either a local instance or a cloud instance (https://console.weaviate.cloud/). Cloud is free for 21 day.
3. Python > 3.10 configured on your machine

# Running bot
1. Create virtual environment
2. Copy .env.template to .env and fill in the values OPEN_AI_LLM_MODEL and OPENAI_API_KEY with the values from your OpenAI account
3. Update WEVIATE_URL in .env to point to the weaviate instance
3. Install requirements `pip install -r requirements.txt`
6. Run `streamlit run chat.py` to start the app in the browser
