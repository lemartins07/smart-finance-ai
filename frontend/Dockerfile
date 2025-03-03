# Usa uma imagem leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários para instalar as dependências
COPY frontend/requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do frontend para dentro do container
COPY frontend/ .

# Expõe a porta onde o Streamlit rodará
EXPOSE 8501

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
