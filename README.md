🚀 Twitter 

📝 Descrição do Projeto

O Twitter Clone é uma aplicação Full Stack desenvolvida para aprofundar conhecimentos em Django Rest Framework, React, Vite, JWT e deploy em nuvem.

O projeto é composto por dois módulos:

Backend (API) → Django Rest Framework
Implantado no PythonAnywhere

Frontend (Interface) → React + Vite
Implantado na Vercel

Durante o desenvolvimento, utilizei Docker + PostgreSQL no ambiente local para maior flexibilidade e escalabilidade, enquanto o deploy utiliza SQLite para manter o backend leve dentro do PythonAnywhere.

✨ Funcionalidades

👤 Autenticação JWT (Login / Registro)

📝 Tweets: Criar, listar, editar e excluir

🔁 Sistema de seguidores

🔔 Notificações básicas

🧑‍💼 Admin do Django para gerenciar a aplicação

🌐 Integração frontend-backend via API

⚡ Front-end rápido com React + Vite

🎨 Estilização com TailwindCSS

📂 Estrutura do Projeto
🖥️ Backend (Django)

Django 5.x

Django Rest Framework

Autenticação via JWT

CORS Headers configurado para integração com Vercel

WhiteNoise para servir arquivos estáticos

Variáveis de ambiente via .env

Banco:

Desenvolvimento: PostgreSQL (Docker)

Produção: SQLite (PythonAnywhere)

🌐 Frontend (React)

React 18 + Vite

Tailwind CSS

React Router

Zustand para gerenciamento de estado

Comunicação via fetch/axios usando:

import.meta.env.VITE_API_URL


Deploy automático pela Vercel

⚙️ Configuração do Ambiente de Desenvolvimento
🔧 Backend
1️⃣ Clonar o repositório
git clone https://github.com/Kaiof7/twitter.git
cd twitter/backend

2️⃣ Criar ambiente virtual
python3.10 -m venv env
source env/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt


(ou poetry install caso use Poetry)

4️⃣ Migrações do banco
python manage.py makemigrations
python manage.py migrate

5️⃣ Criar superusuário
python manage.py createsuperuser

6️⃣ Rodar servidor local
python manage.py runserver

💻 Frontend
1️⃣ Entrar no diretório
cd twitter/frontend

2️⃣ Instalar dependências
npm install

3️⃣ Criar .env com a URL da API
VITE_API_URL=http://localhost:8000


Ou para produção:

VITE_API_URL=https://kaio17.pythonanywhere.com

4️⃣ Rodar servidor de desenvolvimento
npm run dev

☁️ Deploy
🐍 Backend – PythonAnywhere

Hospedado em: https://kaio17.pythonanywhere.com/

Configurado com:

WSGI

ALLOWED_HOSTS

CSRF_TRUSTED_ORIGINS

WhiteNoise

Webhook configurado para receber updates do GitHub (opcional)

⚛️ Frontend – Vercel
Configurações:

Build Command:

npm run build


Install Command:

npm install


Output Directory:

dist


Variáveis de ambiente:

VITE_API_URL=https://kaio17.pythonanywhere.com

🧪 Testes

Para executar os testes automatizados no backend:

python manage.py test

🛠️ Tecnologias Utilizadas
Backend

Django 5.x

Django REST Framework

Simple JWT

WhiteNoise

CORS Headers

Docker

PostgreSQL / SQLite

Frontend

React 18

Vite

Tailwind CSS

React Router

Zustand

Axios / Fetch


👨‍💻 Autor

Matheus costa