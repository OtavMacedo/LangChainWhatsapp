from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Session:
    id: str
    name: Optional[str] = None
    age: Optional[int] = None
    weight_kg: Optional[float] = None
    height_cm: Optional[int] = None
    objective: Optional[str] = None
    experience: Optional[str] = None
    finished: bool = False
    step: Literal['name', 'age', 'weight_kg', 'height_cm', 'objective', 'experience', 'finishing'] = 'name'
