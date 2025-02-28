# SmartFinance AI

SmartFinance AI é um aplicativo de gestão financeira inteligente que utiliza **OCR e IA da OpenAI** para capturar, categorizar e analisar transações financeiras de forma automatizada. O sistema permite que o usuário registre transações por meio de **formulários, imagens, PDFs, áudios e textos**.

## 🚀 Funcionalidades

- 📸 **Cadastro via imagem**: Extração de informações financeiras usando OCR.
- 🤖 **Processamento de transações com IA**: Análise e categorização automática.
- 📂 **Suporte a múltiplos formatos**: Imagens, PDFs, CSVs e áudios.
- 📊 **Dashboard interativo**: Visualização de gastos e insights financeiros.
- 🔍 **Verificação de duplicatas**: Evita registros repetidos.
- 🗂 **Banco de dados integrado**: Gerenciamento eficiente das transações.

## 🏗 Estrutura do Projeto

```
SmartFinanceAI/
│── src/                   # Código-fonte principal
│   │── app.py             # Arquivo principal do Streamlit
│   │── ocr.py             # Lógica de extração de texto de imagens
│   │── ai.py              # Integração com OpenAI
│   │── database.py        # Gerenciamento do banco de dados
│   │── utils.py           # Funções auxiliares
│── models/                # Modelos e schemas de dados
│   │── transaction.py     # Modelo de transação financeira
│── data/                  # Dados e arquivos temporários
│── tests/                 # Testes automatizados
│── requirements.txt       # Dependências do projeto
│── Dockerfile             # Configuração do Docker
│── docker-compose.yml     # Orquestração de serviços
│── .env                   # Variáveis de ambiente
│── README.md              # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas

- **Python 3.12**
- **Streamlit** (Interface gráfica)
- **Tesseract OCR** (Extração de texto de imagens)
- **OpenAI API** (Processamento de transações)
- **SQLite / PostgreSQL** (Banco de dados)
- **Docker & Docker Compose** (Ambiente isolado)

## 📦 Instalação e Configuração

### 🔹 Com Docker

```bash
git clone https://github.com/seuusuario/SmartFinanceAI.git
cd SmartFinanceAI
docker-compose up --build
```

### 🔹 Com Ambiente Virtual (venv)

```bash
git clone https://github.com/lemartins07/SmartFinanceAI.git
cd SmartFinanceAI
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

## 📌 Próximos Passos

- 🔧 Melhorar a categorização automática da IA.
- 📊 Implementar gráficos dinâmicos para insights financeiros.
- 🔐 Criar autenticação de usuários.

## 📄 Licença

Este projeto é open-source e está sob a licença MIT.

