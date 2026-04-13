from fastapi import APIRouter
from app.api.routes import payments, users, escrow

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(escrow.router, prefix="/escrow", tags=["Escrow"])