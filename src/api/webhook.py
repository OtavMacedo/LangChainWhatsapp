import logging

from fastapi import APIRouter, Request, BackgroundTasks

from src.api.schemas import WhatsappEvent
from src.conversation.run import run_conversation_flow

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post('/evolution')
async def hook(req: Request, background_tasks: BackgroundTasks):
    payload = await req.json()

    try:
        event = WhatsappEvent.model_validate(payload)
    except Exception:
        logger.warning("Payload inválido recebido, ignorando.")
        return {"ok": False, "error": "invalid payload"}

    if event.data.key.fromMe:
        return {"ok": True, "skipped": "own message"}

    jid = event.data.key.remoteJid
    user_message = event.data.message.conversation

    background_tasks.add_task(run_conversation_flow, jid, user_message)

    return {"ok": True}
