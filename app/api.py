import base64
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from app.chat_service import chat_stream, memory
from pydantic import BaseModel

router = APIRouter()

from pydantic import BaseModel

class ResetRequest(BaseModel):
    session_id: str


@router.post("/chat")
async def chat_endpoint(
    session_id: str = Form(...),
    message: str = Form(...),
    image: UploadFile | None = File(None)
):
    # ✅ Si viene imagen, convertir a base64 y agregar al mensaje
    if image is not None:
        image_bytes = await image.read()
        b64 = base64.b64encode(image_bytes).decode("utf-8")
        message += f"\n\n[Imagen en base64]: {b64}"

    # ✅ Generador de texto (stream)
    stream_gen = chat_stream(session_id, message)

    # ✅ MUY IMPORTANTE: text/plain (NO text/event-stream)
    return StreamingResponse(
        stream_gen,
        media_type="text/plain; charset=utf-8"
    )



@router.post("/reset")
def reset_session(req: ResetRequest):
    memory.store.pop(req.session_id, None)
    return {"status": "ok"}



@router.get("/health")
def health():
    return {"status": "ok", "service": "RAG Helpdesk"}