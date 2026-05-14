from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import httpx, os

app = FastAPI()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    system: Optional[str] = None
    max_tokens: int = 1500

@app.post("/api/chat")
async def chat(req: ChatRequest):
    if not OPENROUTER_API_KEY:
        raise HTTPException(500, "OPENROUTER_API_KEY not set")
    msgs = []
    if req.system:
        msgs.append({"role": "system", "content": req.system})
    msgs += [{"role": m.role, "content": m.content} for m in req.messages]
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "content-type": "application/json"},
            json={"model": "anthropic/claude-sonnet-4-5", "max_tokens": req.max_tokens, "messages": msgs}
        )
        if r.status_code != 200:
            raise HTTPException(r.status_code, r.text)
        return {"content": r.json()["choices"][0]["message"]["content"]}

@app.get("/health")
def health():
    return {"status": "ok", "key_set": bool(OPENROUTER_API_KEY)}

app.mount("/", StaticFiles(directory="/app/static", html=True), name="static")
