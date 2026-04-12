# StellerGigs-Backend

 Backend Repo: `stellar-gigs-backend`

## 📦 Folder Structure

```bash
stellar-gigs-backend/
│
├── app/
│   ├── main.py              # Entry point
│
│   ├── api/                 # Routes
│   │   ├── routes/
│   │   │   ├── payments.py
│   │   │   ├── users.py
│   │   │   └── escrow.py
│   │   └── router.py
│
│   ├── core/                # Config & settings
│   │   ├── config.py
│   │   └── security.py
│
│   ├── models/              # Data models
│   │   ├── user.py
│   │   └── payment.py
│
│   ├── schemas/             # Pydantic schemas
│   │   ├── user.py
│   │   └── payment.py
│
│   ├── services/            # Business logic
│   │   ├── stellar_service.py
│   │   ├── escrow_service.py
│   │   └── payment_service.py
│
│   ├── db/                  # Database setup
│   │   ├── base.py
│   │   └── session.py
│
│   └── utils/               # Helpers
│       └── helpers.py
│
├── tests/                   # Test files
│
├── .env.example
├── requirements.txt
├── README.md
└── alembic/                 # Migrations (optional)
```

---

# ⚙️ Step 1: Create Project

```bash
mkdir stellar-gigs-backend
cd stellar-gigs-backend
python -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
```

---

# 📦 Step 2: Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv stellar-sdk pydantic
```

Save them:

```bash
pip freeze > requirements.txt
```

---

# 🚀 Step 3: Main App Entry

## `app/main.py`

```python
from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Stellar Gigs API",
    description="Backend for freelance payments platform",
    version="1.0.0"
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Stellar Gigs API is running"}
```

---

# 🔗 Step 4: API Router

## `app/api/router.py`

```python
from fastapi import APIRouter
from app.api.routes import payments, users, escrow

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(escrow.router, prefix="/escrow", tags=["Escrow"])
```

---

# 💳 Step 5: Payment Route Example

## `app/api/routes/payments.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
def create_payment(amount: float, wallet: str):
    return {
        "message": "Payment created",
        "amount": amount,
        "wallet": wallet
    }
```

---

# 🔐 Step 6: Stellar Service

## `app/services/stellar_service.py`

```python
from stellar_sdk import Server, Keypair, TransactionBuilder, Network

server = Server("https://horizon-testnet.stellar.org")


def create_account():
    pair = Keypair.random()
    return {
        "public_key": pair.public_key,
        "secret": pair.secret
    }
```

---

# 🔒 Step 7: Escrow Service (Basic Placeholder)

## `app/services/escrow_service.py`

```python
def create_escrow(amount, client, freelancer):
    return {
        "status": "escrow_created",
        "amount": amount,
        "client": client,
        "freelancer": freelancer
    }
```

---

# ⚙️ Step 8: Config File

## `app/core/config.py`

```python
import os
from dotenv import load_dotenv

load_dotenv()

STELLAR_NETWORK = os.getenv("STELLAR_NETWORK", "testnet")
SECRET_KEY = os.getenv("SECRET_KEY")
```

---

# 🔐 Step 9: Environment File

## `.env.example`

```env
STELLAR_NETWORK=testnet
SECRET_KEY=your_secret_key
PUBLIC_KEY=your_public_key
```

---





