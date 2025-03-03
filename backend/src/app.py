from fastapi import FastAPI

from backend.src.routes import (
    category_routes,
    subcategory_routes,
    user_routes,
    transaction_routes,
)

app = FastAPI(title="SmartFinanceAI API", version="1.0.0")

# Rotas
app.include_router(transaction_routes.router)
app.include_router(category_routes.router)
app.include_router(subcategory_routes.router)
app.include_router(user_routes.router)


@app.get("/")
async def root():
    return {"message": "🚀 SmartFinance API rodando!"}
