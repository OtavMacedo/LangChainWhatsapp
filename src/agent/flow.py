from agent.model import get_model
from agent.prompts import ASK_NAME_PROMPT


async def ask_name():
    model = get_model()
    model_response = await model.ainvoke(ASK_NAME_PROMPT)
    return model_response.text
