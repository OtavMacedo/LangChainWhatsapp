from typing import Optional, TypeVar, Type

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from agent.model import get_model
from agent.prompts import GET_AGE_PROMPT, GET_EXPERIENCE_PROMPT, GET_HEIGHT_PROMPT, GET_NAME_PROMPT, GET_OBJECTIVE_PROMPT, GET_WEIGHT_PROMPT
from agent.schemas import ExtractAgeOutput, ExtractExperienceOutput, ExtractHeightOutput, ExtractNameOutput, ExtractObjectiveOutput, ExtractWeightOutput

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


async def extract_name(user_message: str) -> Optional[float]:
    result = await extract_structured(
        user_message,
        ExtractNameOutput,
        GET_NAME_PROMPT
    )
    return result.name


async def extract_age(user_message: str) -> Optional[float]:
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


async def test_extractions():
    """Testa todas as funções de extração"""
    
    # Teste de peso
    print("=== PESO ===")
    print(await extract_weight("peso 75kg"))  # 75.0
    print(await extract_weight("estou com 80 quilos"))  # 80.0
    print(await extract_weight("meu peso é 68.5"))  # 68.5
    print(await extract_weight("não sei"))  # None
    
    # Teste de altura
    print("\n=== ALTURA ===")
    print(await extract_height("1,75m"))  # 175
    print(await extract_height("tenho 1,80 de altura"))  # 180
    print(await extract_height("175cm"))  # 175
    print(await extract_height("não sei"))  # None
    
    # Teste de objetivo
    print("\n=== OBJETIVO ===")
    print(await extract_objective("quero ganhar massa"))  # "ganhar massa"
    print(await extract_objective("preciso emagrecer"))  # "emagrecer"
    print(await extract_objective("quero definir o corpo"))  # "definição"
    print(await extract_objective("melhorar condicionamento"))  # "condicionamento"
    print(await extract_objective("não sei ainda"))  # None
    
    # Teste de experiência
    print("\n=== EXPERIÊNCIA ===")
    print(await extract_experience("nunca treinei"))  # "iniciante"
    print(await extract_experience("treino há 2 anos"))  # "intermediário"
    print(await extract_experience("sou atleta"))  # "avançado"
    print(await extract_experience("não sei dizer"))  # None