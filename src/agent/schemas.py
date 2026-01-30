from typing import Optional
from pydantic import BaseModel, Field


class ExtractNameOutput(BaseModel):
    name: str = Field(..., description='O primeiro nome da pessoa, capitalizado')


class ExtractAgeOutput(BaseModel):
    age: Optional[int] = Field(None, description='A idade da pessoa (entre 0 e 120 anos)')


class ExtractWeightOutput(BaseModel):
    weight_kg: Optional[float] = Field(
        None,
        description='Peso em quilogramas (ex: 75.5). Null se não conseguir identificar.'
    )


class ExtractHeightOutput(BaseModel):
    height_cm: Optional[int] = Field(
        None,
        description='Altura em centímetros (ex: 175). Null se não conseguir identificar.'
    )


class ExtractObjectiveOutput(BaseModel):
    objective: Optional[str] = Field(
        None,
        description='Objetivo fitness do cliente (ex: "ganhar massa", "emagrecer", "definição", "condicionamento")'
    )


class ExtractExperienceOutput(BaseModel):
    experience: Optional[str] = Field(
        None,
        description='Nível de experiência com treinos: "iniciante", "intermediário" ou "avançado"'
    )
