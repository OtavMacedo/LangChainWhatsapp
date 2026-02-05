import logging
import os
from pathlib import Path

import httpx

from src.agent.flow import (
    ask_something,
    extract_age, extract_experience, extract_height,
    extract_name, extract_objective, extract_weight,
)
from src.agent.prompts import (
    WELCOME_PROMPT, ASK_AGE_PROMPT, ASK_EXPERIENCE_PROMPT,
    ASK_HEIGHT_PROMPT, ASK_OBJECTIVE_PROMPT, ASK_WEIGHT_PROMPT,
    FAREWELL_PROMPT,
)
from src.agent.session import Session, get_or_create_session

logger = logging.getLogger(__name__)

EVOLUTION_API_URL = os.getenv("EVOLUTION_API_URL", "http://evolution_api:8080")
EVOLUTION_INSTANCE = os.getenv("EVOLUTION_INSTANCE", "default")
EVOLUTION_API_KEY = os.getenv("AUTHENTICATION_API_KEY", "")

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


async def send_text(jid: str, text: str):
    url = f"{EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE}"
    headers = {"apikey": EVOLUTION_API_KEY, "Content-Type": "application/json"}
    payload = {"number": jid, "text": text}
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()


async def send_video(jid: str, video_path: Path):
    url = f"{EVOLUTION_API_URL}/message/sendMedia/{EVOLUTION_INSTANCE}"
    headers = {"apikey": EVOLUTION_API_KEY, "Content-Type": "application/json"}

    import base64
    video_bytes = video_path.read_bytes()
    video_b64 = base64.b64encode(video_bytes).decode()

    payload = {
        "number": jid,
        "mediatype": "video",
        "media": video_b64,
        "fileName": video_path.name,
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()


def _find_video() -> Path | None:
    if not ASSETS_DIR.exists():
        return None
    for ext in ("*.mp4", "*.mov", "*.avi", "*.mkv"):
        files = list(ASSETS_DIR.glob(ext))
        if files:
            return files[0]
    return None


async def run_conversation_flow(jid: str, user_message: str):
    session = get_or_create_session(jid)

    if session.finished:
        return

    try:
        await _process_step(session, user_message)
    except Exception:
        logger.exception("Erro ao processar step '%s' para jid '%s'", session.step, jid)


async def _process_step(session: Session, user_message: str):
    step = session.step
    jid = session.id

    # ── ASK steps: gera mensagem com LLM e envia, depois avança para GET ──
    if step == "ask_name":
        reply = await ask_something(WELCOME_PROMPT)
        await send_text(jid, reply)
        session.next_step()  # -> get_name
        return

    if step == "get_name":
        name = await extract_name(user_message)
        if name:
            session.name = name
            session.next_step()  # -> ask_age
            await _process_step(session, user_message)  # imediatamente pede a idade
        else:
            from src.agent.prompts import ASK_NAME_PROMPT
            reply = await ask_something(ASK_NAME_PROMPT)
            await send_text(jid, reply)
        return

    if step == "ask_age":
        reply = await ask_something(ASK_AGE_PROMPT.format(name=session.name))
        await send_text(jid, reply)
        session.next_step()  # -> get_age
        return

    if step == "get_age":
        age = await extract_age(user_message)
        if age:
            session.age = age
            session.next_step()  # -> ask_weight
            await _process_step(session, user_message)
        else:
            reply = await ask_something(ASK_AGE_PROMPT.format(name=session.name))
            await send_text(jid, reply)
        return

    if step == "ask_weight":
        reply = await ask_something(ASK_WEIGHT_PROMPT.format(name=session.name))
        await send_text(jid, reply)
        session.next_step()  # -> get_weight
        return

    if step == "get_weight":
        weight = await extract_weight(user_message)
        if weight:
            session.weight_kg = weight
            session.next_step()  # -> ask_height
            await _process_step(session, user_message)
        else:
            reply = await ask_something(ASK_WEIGHT_PROMPT.format(name=session.name))
            await send_text(jid, reply)
        return

    if step == "ask_height":
        reply = await ask_something(ASK_HEIGHT_PROMPT.format(name=session.name))
        await send_text(jid, reply)
        session.next_step()  # -> get_height
        return

    if step == "get_height":
        height = await extract_height(user_message)
        if height:
            session.height_cm = height
            session.next_step()  # -> ask_objective
            await _process_step(session, user_message)
        else:
            reply = await ask_something(ASK_HEIGHT_PROMPT.format(name=session.name))
            await send_text(jid, reply)
        return

    if step == "ask_objective":
        reply = await ask_something(ASK_OBJECTIVE_PROMPT.format(name=session.name))
        await send_text(jid, reply)
        session.next_step()  # -> get_objective
        return

    if step == "get_objective":
        objective = await extract_objective(user_message)
        if objective:
            session.objective = objective
            session.next_step()  # -> ask_experience
            await _process_step(session, user_message)
        else:
            reply = await ask_something(ASK_OBJECTIVE_PROMPT.format(name=session.name))
            await send_text(jid, reply)
        return

    if step == "ask_experience":
        reply = await ask_something(ASK_EXPERIENCE_PROMPT.format(name=session.name))
        await send_text(jid, reply)
        session.next_step()  # -> get_experience
        return

    if step == "get_experience":
        experience = await extract_experience(user_message)
        if experience:
            session.experience = experience
            session.next_step()  # -> farewell
            await _process_step(session, user_message)
        else:
            reply = await ask_something(ASK_EXPERIENCE_PROMPT.format(name=session.name))
            await send_text(jid, reply)
        return

    if step == "farewell":
        reply = await ask_something(FAREWELL_PROMPT.format(name=session.name))
        await send_text(jid, reply)

        video = _find_video()
        if video:
            await send_video(jid, video)

        session.next_step()
        session.finished = True

        logger.info(
            "Qualificação finalizada — jid=%s name=%s age=%s weight=%s height=%s objective=%s experience=%s",
            jid, session.name, session.age, session.weight_kg,
            session.height_cm, session.objective, session.experience,
        )
        return
