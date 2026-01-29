from dataclasses import dataclass
from typing import Literal


@dataclass
class Session:
    id: str
    name: str
    age: int
    weight_kg: float
    height_cm: int
    objective: str
    experience: str
    finished: bool
    step: Literal['name', 'age', 'weight_kg', 'height_cm', 'objective', 'experience', 'finishing']
