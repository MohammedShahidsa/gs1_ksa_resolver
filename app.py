from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="GS1 Saudi Resolver",
    version="1.0.0"
)

# NPC_BASE = "https://npc.gs1.org.sa"
NPC_BASE = os.getenv("NPC_BASE")


@app.api_route("/{path:path}", methods=["GET", "POST"])
async def resolver(request: Request, path: str):
    query = request.url.query

    target = f"{NPC_BASE}/{path}"

    if query:
        target += f"?{query}"

    return RedirectResponse(
        url=target,
        status_code=302
    )