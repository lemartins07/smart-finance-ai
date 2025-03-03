# Usa uma imagem leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários para instalar as dependências
COPY backend/requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do backend para dentro do container
COPY backend/ .

# Expõe a porta onde o FastAPI rodará
EXPOSE 8000

# Comando para iniciar o FastAPI com Uvicorn
CMD ["python", "-m", "uvicorn", "backend.src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

