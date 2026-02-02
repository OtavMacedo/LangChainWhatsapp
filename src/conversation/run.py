from src.agent.flow import ask_something, extract_age, extract_experience, extract_height, extract_name, extract_objective, extract_weight
from src.agent.prompts import ASK_AGE_PROMPT, ASK_EXPERIENCE_PROMPT, ASK_HEIGHT_PROMPT, ASK_NAME_PROMPT, ASK_OBJECTIVE_PROMPT, ASK_WEIGHT_PROMPT
from src.agent.session import Session


steps_callback = {
    'ask_name': lambda: ask_something(ASK_NAME_PROMPT),
    'get_name': extract_name,
    'ask_age': lambda: ask_something(ASK_AGE_PROMPT),
    'get_age': extract_age,
    'ask_weight': lambda: ask_something(ASK_WEIGHT_PROMPT),
    'get_weight': extract_weight,
    'ask_height': lambda: ask_something(ASK_HEIGHT_PROMPT),
    'get_height': extract_height,
    'ask_objective': lambda: ask_something(ASK_OBJECTIVE_PROMPT),
    'get_objective': extract_objective,
    'ask_experience': lambda: ask_something(ASK_EXPERIENCE_PROMPT),
    'get_experience': extract_experience,
    'send_instruction': ...,
}

def create_session(jid: str):
    return Session(id=jid)

def get_session(jid: str):
    return create_session(jid)

def run_conversation_flow(jid):
    session = get_session(jid)
    pass