# 🎮 Human.exe- Screen Login + Steam (Human.exe)

Uma plataforma de jogos inspirada no Steam, desenvolvida com **React + Vite** (Frontend) e **FastAPI** (Backend), integrada com **Oracle Database**.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+** 
- **Node.js 16+** e **npm**
- **Oracle Database** (acessível via rede)
- **Git**

## 🚀 Como Rodar o Projeto

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
cd humanPlay/game-starter
```

### 2. Configurar o Backend (API)

#### 2.1 Instalar Dependências Python

```bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

#### 2.2 Configurar Banco de Dados

Edite o arquivo `config.py` com suas credenciais do Oracle:

```python
# Exemplo de configuração
DATABASE_URL = "usuario/senha@oracle.fiap.com.br:1521/orcl"
```

#### 2.3 Executar a API

```bash
python main.py
```

A API estará disponível em: **http://localhost:8000**

### 3. Configurar o Frontend (React)

#### 3.1 Instalar Dependências Node.js

```bash
# Instalar dependências
npm install
```

#### 3.2 Executar o Frontend

```bash
npm run dev
```

O frontend estará disponível em: **http://localhost:5173**

## 🌐 Acessos

- **Frontend:** http://localhost:5173
- **API:** http://localhost:8000
- **Documentação da API:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📁 Estrutura do Projeto

```
game-starter/
├── 📁 app/                    # Backend FastAPI
│   ├── 📁 controllers/        # Rotas da API
│   ├── 📁 models/            # Modelos Pydantic
│   ├── 📁 services/          # Lógica de negócio
│   └── database.py           # Configuração do banco
├── 📁 src/                   # Frontend React
│   ├── 📁 pages/             # Páginas da aplicação
│   ├── 📁 services/          # Serviços de API
│   └── 📁 assets/            # Imagens e recursos
├── 📄 main.py                # Servidor principal
├── 📄 config.py              # Configurações
├── 📄 requirements.txt       # Dependências Python
└── 📄 package.json           # Dependências Node.js
```

## 🎯 Funcionalidades

### ✅ Implementadas
- **Autenticação de usuários** com Oracle Database
- **Interface Steam-like** com React
- **Sistema de login/logout** com auditoria
- **Páginas responsivas** (Home, Details, Login, Signup)
- **API REST** completa com FastAPI
- **Validação de dados** com Pydantic

### 🔄 Em Desenvolvimento
- Sistema de compra de jogos
- Biblioteca pessoal de jogos
- Sistema de avaliações
- Chat em tempo real

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno
- **Oracle Database** - Banco de dados
- **Pydantic** - Validação de dados
- **bcrypt** - Hash de senhas
- **uvicorn** - Servidor ASGI

### Frontend
- **React 18** - Biblioteca de interface
- **Vite** - Build tool e dev server
- **React Router** - Roteamento
- **CSS3** - Estilização

## 📊 Banco de Dados

### Tabelas Principais
- **CP01_2S_PERFIL** - Perfis de usuário
- **CP01_2S_USUARIO** - Dados dos usuários
- **CP01_2S_LOGIN** - Auditoria de logins

### Scripts SQL
Execute no Oracle Database:

```sql
-- Criar tabelas (se não existirem)
CREATE TABLE CP01_2S_PERFIL (
    ID_PERFIL NUMBER PRIMARY KEY,
    NOME_PERFIL VARCHAR2(100) NOT NULL,
    DESC_PERFIL VARCHAR2(200) NOT NULL
);

CREATE TABLE CP01_2S_USUARIO (
    ID_USUARIO NUMBER PRIMARY KEY,
    NOME_USUARIO VARCHAR2(120) NOT NULL,
    EMAIL VARCHAR2(120) NOT NULL UNIQUE,
    SENHA_USUARIO VARCHAR2(500) NOT NULL,
    APELIDO_STEAM VARCHAR2(60) NOT NULL,
    DATA_CRIACAO DATE NOT NULL,
    ULTIMO_LOGIN DATE,
    ID_PERFIL NUMBER NOT NULL,
    FOREIGN KEY (ID_PERFIL) REFERENCES CP01_2S_PERFIL(ID_PERFIL)
);

CREATE TABLE CP01_2S_LOGIN (
    ID_LOGIN NUMBER PRIMARY KEY,
    IP_LOGIN VARCHAR2(45) NOT NULL,
    USER_AGENT VARCHAR2(400) NOT NULL,
    DATA_LOGIN DATE NOT NULL,
    ID_USUARIO NUMBER NOT NULL,
    FOREIGN KEY (ID_USUARIO) REFERENCES CP01_2S_USUARIO(ID_USUARIO)
);

-- Inserir perfil padrão
INSERT INTO CP01_2S_PERFIL VALUES (1, 'Usuario', 'Perfil de usuario comum');
COMMIT;
```

## 🔧 Comandos Úteis

### Backend
```bash
# Executar API
python main.py

# Instalar dependência específica
pip install fastapi

# Verificar versão Python
python --version
```

### Frontend
```bash
# Executar em modo desenvolvimento
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview

# Instalar dependência
npm install react-router-dom
```

## 🐛 Solução de Problemas

### Erro de Conexão Oracle
- Verifique se o Oracle está rodando
- Confirme as credenciais no `config.py`
- Teste a conectividade: `telnet oracle.fiap.com.br 1521`

### Erro de Dependências Python
```bash
# Limpar cache do pip
pip cache purge

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### Erro de Dependências Node.js
```bash
# Limpar cache do npm
npm cache clean --force

# Deletar node_modules e reinstalar
rm -rf node_modules package-lock.json
npm install
```

### CORS Error
- Verifique se a API está rodando na porta 8000
- Confirme se o frontend está na porta 5173
- Teste a API diretamente: http://localhost:8000/docs

## 📝 Scripts de Desenvolvimento

### Executar Tudo (Backend + Frontend)
```bash
# Terminal 1 - Backend
python main.py

# Terminal 2 - Frontend  
npm run dev
```

### Testar API
```bash
# Health check
curl http://localhost:8000/health

# Listar usuários
curl http://localhost:8000/usuarios/
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é para fins acadêmicos.

