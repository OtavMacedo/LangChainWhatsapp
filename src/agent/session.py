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
    step: Literal[
        'ask_name',
        'get_name',
        'ask_age',
        'get_age',
        'ask_weight',
        'get_weight',
        'ask_height',
        'get_height',
        'ask_objective',
        'get_objective',
        'ask_experience',
        'get_experience',
        'send_instruction',
        'finished'
    ] = 'name'
