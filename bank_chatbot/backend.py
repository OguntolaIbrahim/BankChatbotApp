import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import openai
import openai.error

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the .env file.")

def check_openai_connection():
    try:
        openai.Model.list()
    except openai.error.OpenAIError as e:
        raise ConnectionError("Failed to connect to OpenAI API. Please check your internet connection and API key.") from e

# Call this function during initialization to ensure connectivity
check_openai_connection()

chat_model = ChatOpenAI(api_key=OPENAI_API_KEY)
conversation_memory = ConversationBufferMemory()
conversation_chain = ConversationChain(llm=chat_model, memory=conversation_memory)

def get_response(user_input, history):
    return conversation_chain.run(input=user_input)