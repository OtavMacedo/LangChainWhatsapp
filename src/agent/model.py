from langchain.chat_models import init_chat_model

def get_model(temperature=0):
    return init_chat_model(model='openai:gpt-5-mini', temperature=temperature)
