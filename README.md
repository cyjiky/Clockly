# Clockly

## Description

Clockly is a mobile calendar application. The project is designed to be an advanced alternative to Google Calendar, offering extended functionality such as custom summaries for selected timeframes, flexible configuration, and other additional features.

## Stack

<div style="display:flex; gap:10px; align-items:center;">
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/reactnative/reactnative-original-wordmark.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg" />  
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/expo/expo-line.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" />
</div>

### Backend

- fastAPI
- Pydantic

### Frontend

- React Native
- Expo

## Structure

```text
📁.                                 project folder
 ├── 📁 backend                     server-side logic
 |    ├── 📁 auth                   authentication & authorization
 |    ├── 📁 DTOs                   data transfer objects
 |    ├── 📁 routers                api route definition
 |    ├── 📁 postgre                postgres setup via SQLAlchemy
 |    ├── 📁 services               logic layer
 |    ├── 📁 utils                  shared helper functions
 |    ├── 📝 main.py                backend entry point
 |    ├── ⚙️ .env.example           environment variables
 |    ├── 🐳 Containerfile          backend container build
 |    └── 📝 pyproject.toml         python dependencies & config
 ├── 📁 frontend                    client-side application
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    ├── 📁 constants              global constants & configurations
 |    ├── 📁 hooks                  custom state & lifecycle hooks
 |    ├── 📝 package.json           frontend dependencies & scripts
 |    └── 🐳 Containerfile          frontend container build
 ├── 🐳 compose.yaml                docker compose orchestration
 ├── 📄LICENCE                      LICENCE
 └── 📍README.md                    project description
```


## Usage

To run the application, follow these steps:

```bash
git clone https://github.com/cyjiky/Clockly.git

cd Clockly # Move to repository directory
```

### Using Docker Compose

**Run `compose.yaml`**

```bash
docker compose up
```

### How to use DB-UI?
-> TODO 

### Manually 
-> TODO (links)



## Features & Future Roadmap
-> TODO

```mermaid
journey
  title Clockly roadmap
  section Backend
    OAuth 2.0: 2
    Visualization API: 5
    Calendar API: 7
  section Frontend
    Fetching: 2
    Components implementstions: 5
    DB: 0
```

---


## Project status

The project is currently under development

---

<div align="display:flex; gap:10px; align-items:center;">

**Authors**  
[@cyjiky](https://github.com/cyjiky) $\cdot$ [@yeghor](https://github.com/yeghor)

</div>
