# 🚀 Backend - Steam Games API

Este é o backend da aplicação de exemplo de como o jogo (Human.exe) ficaria na steam, construído com **FastAPI** e conectado ao **Oracle Database**.

## 📋 Deploy no Vercel

### 1. Conectar ao Vercel
- Acesse [vercel.com](https://vercel.com)
- Crie um novo projeto
- Conecte este repositório (pasta backend)

### 2. Configurar Variáveis de Ambiente
No painel do Vercel, adicione estas variáveis:

```
DB_USER=seu_usuario_oracle
DB_PASSWORD=sua_senha_oracle
DB_HOST=oracle.fiap.com.br
DB_PORT=1521
DB_SID=ord
SESSION_TIMEOUT_MINUTES=30
```

### 3. Deploy
- Clique em "Deploy"
- Aguarde o build completar
- Sua API estará disponível em: `https://seu-projeto.vercel.app`

## 🔧 Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python main.py
```

A API estará disponível em: `http://localhost:8000`

## 📊 Endpoints da API

- `GET /` - Informações da API
- `GET /health` - Health check
- `GET /docs` - Documentação Swagger
- `POST /auth/login` - Login de usuário
- `GET /usuarios/` - Listar usuários
- `POST /usuarios/` - Criar usuário
- `GET /logins/` - Listar logins (auditoria)

## 🛠️ Tecnologias

- **FastAPI** - Framework web
- **Oracle Database** - Banco de dados
- **Pydantic** - Validação de dados
- **bcrypt** - Hash de senhas
- **uvicorn** - Servidor ASGI
