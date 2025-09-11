# 🎨 Frontend - Steam Games

Este é o frontend da aplicação de exemplo de como o jogo (Human.exe) ficaria na steam, construído com **React + Vite**.

## 📋 Deploy no Vercel

### 1. Conectar ao Vercel
- Acesse [vercel.com](https://vercel.com)
- Crie um novo projeto
- Conecte este repositório (pasta frontend)

### 2. Configurar Variáveis de Ambiente
No painel do Vercel, adicione esta variável:

```
VITE_API_URL=https://seu-backend.vercel.app
```
*Substitua pela URL real do seu backend*

### 3. Deploy
- Clique em "Deploy"
- Aguarde o build completar
- Seu site estará disponível em: `https://seu-projeto.vercel.app`

## 🔧 Desenvolvimento Local

```bash
# Instalar dependências
npm install

# Executar servidor de desenvolvimento
npm run dev
```

O site estará disponível em: `http://localhost:5173`

## 📱 Páginas

- **Home** - Página principal com jogos
- **Login** - Autenticação de usuário
- **Signup** - Cadastro de usuário
- **Details** - Detalhes dos jogos

## 🛠️ Tecnologias

- **React 18** - Biblioteca de interface
- **Vite** - Build tool e dev server
- **React Router** - Roteamento
- **CSS3** - Estilização
