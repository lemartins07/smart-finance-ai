import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")


settings = Settings()
