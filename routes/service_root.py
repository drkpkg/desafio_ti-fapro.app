from datetime import datetime

import requests
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    """
    Health check
    """
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{datetime.now().year}.htm"
    response = requests.get(url)
    return {"status": response.status_code, "url": url}
