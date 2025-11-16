# 🤖 ChatCall AI

> **⚠️ Status do Projeto: Em Desenvolvimento ⚠️**
>
> Este projeto é um trabalho em progresso. As funcionalidades principais de chat e salvamento de histórico estão implementadas, mas novos recursos (listados no Roadmap) estão sendo ativamente desenvolvidos.

Bem-vindo ao ChatCall AI, um aplicativo de chat full-stack que se conecta a um modelo de IA local (via Ollama) para conversas em tempo real. Todo o histórico da conversa é salvo e carregado a partir de um banco de dados PostgreSQL.

Este projeto serve como um *template* completo para construir aplicações de IA usando o "stack" FastAPI (Python) e React (TypeScript).

---

## 🎨 Funcionalidades Atuais

* **Chat em Tempo Real:** Converse com o modelo de IA **Mistral** (ou outro) rodando localmente via Ollama.
* **Backend em FastAPI:** Uma API robusta em Python para servir como cérebro da aplicação.
* **Frontend em React (Vite):** Uma interface de usuário moderna, rápida e reativa, construída com TypeScript.
* **Persistência de Dados:** O histórico completo do chat é salvo em um banco PostgreSQL.
* **Carregamento de Histórico:** Ao abrir o app, o histórico de chat anterior é carregado automaticamente.
* **UI Limpa:** Estilização feita com TailwindCSS.
* **Gerenciamento de Estado:** O estado do frontend é gerenciado de forma limpa usando React Context.

---

## 🗺️ Roadmap (Funcionalidades Planejadas)

O futuro deste projeto inclui:

* **Múltiplos Chats:** Permitir que o usuário crie e gerencie várias sessões de chat separadas (ex: "Chat sobre Python", "Chat sobre História").
* **Chat com Documentos (RAG):** Capacidade de fazer upload de um PDF e conversar com a IA sobre o conteúdo específico daquele documento.
* **Gerenciamento de Conversas:** Funcionalidades para renomear e apagar chats salvos.
* **Autenticação de Usuário:** (Opcional) Sistema de login para salvar chats na nuvem.

---

## 🛠️ Stack de Tecnologias

Este projeto é um "monorepo" dividido em duas partes principais:

### Backend (`/backend`)
* **Python 3.12+**
* **FastAPI:** Para a criação da API REST.
* **LangChain:** Para se comunicar com o modelo de linguagem.
* **Ollama:** Para rodar os modelos de LLM localmente.
* **PostgreSQL:** Como banco de dados para salvar o histórico.
* **SQLAlchemy:** Como ORM para se comunicar com o PostgreSQL.

### Frontend (`/frontend`)
* **Vite:** Para "buildar" o projeto React.
* **React:** Para a construção da interface de usuário.
* **TypeScript:** Para adicionar tipagem estática ao código.
* **TailwindCSS:** Para estilização da UI.
* **React Context:** Para gerenciamento de estado global.

---

## ⚙️ Configuração de Variáveis de Ambiente (.env)

Este projeto usa arquivos `.env` para gerenciar segredos e configurações. Você **deve** criá-los antes de rodar.

### 1. Backend (`/backend/.env`)

O backend precisa de um arquivo `.env` para se conectar ao banco de dados PostgreSQL.

1.  Na pasta `/backend`, crie um novo arquivo chamado `.env`.
2.  Adicione a sua string de conexão do banco:

    ```ini
    # /backend/.env
    DATABASE_URL="postgresql://SEU_USUARIO:SUA_SENHA@localhost/chat_call_db"
    ```
    *(Substitua `SEU_USUARIO`, `SUA_SENHA` e `chat_call_db` pelos seus dados reais do PostgreSQL.)*

### 2. Frontend (`/frontend/.env`)

O frontend precisa de um arquivo `.env` para saber onde o backend está rodando.

1.  Na pasta `/frontend`, crie um novo arquivo chamado `.env`.
2.  Adicione a URL base da sua API FastAPI:

    ```ini
    # /frontend/.env
    VITE_API_BASE_URL="[http://127.0.0.1:8000/api/v1](http://127.0.0.1:8000/api/v1)"
    ```
    *(**Importante:** No Vite, todas as variáveis de ambiente expostas ao navegador **devem** começar com o prefixo `VITE_`.)*

---

## 🚀 Como Rodar o Projeto

Para rodar este projeto, você precisará de **três** terminais: um para o Backend, um para o Frontend e um para garantir que o Ollama esteja rodando.

### Pré-requisitos
* **Git**
* **Python 3.10+** (e `pip`)
* **Node.js v18+** (e `npm`)
* **Ollama:** [Baixe e instale o Ollama](https://ollama.com/).
* **Um Modelo de IA:** Após instalar o Ollama, puxe o Mistral: `ollama pull mistral`
* **PostgreSQL:** Um servidor PostgreSQL rodando localmente.

---

### 1. Configuração do Backend (Terminal 1)

1.  **Crie seu Banco de Dados:**
    * No seu PostgreSQL, crie um novo banco de dados (ex: `CREATE DATABASE chat_call_db;`).
    
2.  **Navegue até a pasta do backend:**
    ```bash
    cd backend
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Crie as Tabelas no Banco:**
    (Após ter configurado o `.env` do backend, rode este comando uma vez)
    ```bash
    python create_tables.py
    ```

6.  **Inicie o Servidor Backend:**
    ```bash
    uvicorn app.main:app --reload
    ```
    * O servidor estará rodando em `http://127.0.0.1:8000`

---

### 2. Configuração do Frontend (Terminal 2)

1.  **Abra um *novo terminal*** e navegue até a pasta do frontend:
    ```bash
    cd frontend
    ```

2.  **Instale as dependências:**
    ```bash
    npm install
    ```

3.  **Inicie o Servidor de Desenvolvimento:**
    (Isso lerá seu arquivo `.env` do frontend)
    ```bash
    npm run dev
    ```
    * O servidor estará rodando em `http://localhost:5173` (ou outra porta indicada).

---

### 3. Garanta que o Ollama esteja Rodando

1.  Inicie o aplicativo **Ollama** no seu computador (ele deve aparecer na barra de tarefas).
2.  Certifique-se de que o modelo "mistral" está disponível.

### 4. Use o Aplicativo!
Abra `http://localhost:5173` no seu navegador. O frontend carregará o histórico e você poderá começar a conversar.