from fastapi import APIRouter, Request

from .schemas import WhatsappEvent

router = APIRouter()

@router.post('/evolution')
async def hook(req: Request):
    payload = await req.json()
    print(WhatsappEvent.model_validate(payload))
    return {"ok": True}
