from dataclasses import dataclass
from typing import Dict, Literal, Optional


STEPS = [
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
    'farewell',
    'finished',
]

StepType = Literal[
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
    'farewell',
    'finished',
]


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
    step: StepType = 'ask_name'

    def next_step(self):
        idx = STEPS.index(self.step)
        if idx + 1 < len(STEPS):
            self.step = STEPS[idx + 1]


_sessions: Dict[str, Session] = {}


def get_or_create_session(jid: str) -> Session:
    if jid not in _sessions:
        _sessions[jid] = Session(id=jid)
    return _sessions[jid]
