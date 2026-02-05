from typing import Optional, TypeVar, Type

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from src.agent.model import get_model
from src.agent.prompts import (
    GET_AGE_PROMPT, GET_EXPERIENCE_PROMPT, GET_HEIGHT_PROMPT,
    GET_NAME_PROMPT, GET_OBJECTIVE_PROMPT, GET_WEIGHT_PROMPT,
)
from src.agent.outputs import (
    ExtractAgeOutput, ExtractExperienceOutput, ExtractHeightOutput,
    ExtractNameOutput, ExtractObjectiveOutput, ExtractWeightOutput,
)

T = TypeVar('T', bound=BaseModel)


async def ask_something(prompt):
    model = get_model()
    model_response = await model.ainvoke(prompt)
    return model_response.text


async def extract_structured(
    user_message: str,
    output_model: Type[T],
    system_prompt: str
) -> T:
    model = get_model()
    structured_model = model.with_structured_output(output_model)
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{user_message}")
    ])
    chain = prompt | structured_model
    result: T = await chain.ainvoke({"user_message": user_message})
    return result


async def extract_name(user_message: str) -> Optional[str]:
    result = await extract_structured(
        user_message,
        ExtractNameOutput,
        GET_NAME_PROMPT
    )
    return result.name


async def extract_age(user_message: str) -> Optional[int]:
    result = await extract_structured(
        user_message,
        ExtractAgeOutput,
        GET_AGE_PROMPT
    )
    return result.age


async def extract_weight(user_message: str) -> Optional[float]:
    result = await extract_structured(
        user_message,
        ExtractWeightOutput,
        GET_WEIGHT_PROMPT
    )
    return result.weight_kg


async def extract_height(user_message: str) -> Optional[int]:
    result = await extract_structured(
        user_message,
        ExtractHeightOutput,
        GET_HEIGHT_PROMPT
    )
    return result.height_cm


async def extract_objective(user_message: str) -> Optional[str]:
    result = await extract_structured(
        user_message,
        ExtractObjectiveOutput,
        GET_OBJECTIVE_PROMPT
    )
    return result.objective


async def extract_experience(user_message: str) -> Optional[str]:
    result = await extract_structured(
        user_message,
        ExtractExperienceOutput,
        GET_EXPERIENCE_PROMPT
    )
    return result.experience
