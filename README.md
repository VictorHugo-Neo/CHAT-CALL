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