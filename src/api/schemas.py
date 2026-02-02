from pydantic import BaseModel


class WhatsappEventMessage(BaseModel):
    model_config={'extra': 'ignore'}
    conversation: str

class WhatsappEventKey(BaseModel):
    model_config={'extra': 'ignore'}
    remoteJid: str
    remoteJidAlt: str
    fromMe: bool

class WhatsappEventData(BaseModel):
    model_config={'extra': 'ignore'}
    key: WhatsappEventKey
    message: WhatsappEventMessage
    messageTimestamp: int


class WhatsappEvent(BaseModel):
    model_config={'extra': 'ignore'}
    data: WhatsappEventData
    apikey: str

