from fastapi import FastAPI

from backend.src.routes import category_routes, subcategory_routes
from backend.src.routes import transaction_routes

# from backend.src.routes import

app = FastAPI(title="SmartFinanceAI API", version="1.0.0")

# Rotas
app.include_router(transaction_routes.router)
app.include_router(category_routes.router)
app.include_router(subcategory_routes.router)


@app.get("/")
async def root():
    return {"message": "🚀 SmartFinance API rodando!"}
