
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_escrow():
    return {"message": "Escrow endpoint working"}