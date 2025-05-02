from fastapi import APIRouter, Query
import httpx
from typing import Optional

router = APIRouter(prefix="/media", tags=["media"])

OPENVERSE_BASE_URL = "https://api.openverse.org/v1"

@router.get("/search")
async def search_media(
    q: str = Query(..., description="Search query"),
    type: str = Query("image", description="Type: 'image' or 'audio'"),
    license: Optional[str] = None,
    source: Optional[str] = None
):
    if type not in ["image", "audio"]:
        return {"error": "Invalid media type"}

    params = {"q": q}
    if license:
        params["license"] = license
    if source:
        params["source"] = source

    url = f"{OPENVERSE_BASE_URL}/{type}s"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
        return {"error": "Failed to fetch from Openverse"}

    return response.json()
