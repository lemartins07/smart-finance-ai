from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.src.config.settings import settings

# Definição da base de dados
Base = declarative_base()

# Criando a conexão com o PostgreSQL
engine = create_engine(settings.DATABASE_URL, echo=True)

# Criando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
