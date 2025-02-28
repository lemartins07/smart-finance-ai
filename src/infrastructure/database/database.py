import psycopg2
from config.settings import settings

try:
    conn = psycopg2.connect(settings.DATABASE_URL)
    print("Conectado ao banco de dados com sucesso!")
except Exception as e:
    print("Erro ao conectar no banco:", e)
