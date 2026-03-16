# Clockly

## Description

Clockly is a mobile calendar application. The project is designed to be an advanced alternative to Google Calendar, offering extended functionality such as custom summaries for selected timeframes, flexible configuration, and other additional features.

## Stack

<div style="display:flex; gap:10px; align-items:center;">
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/reactnative/reactnative-original-wordmark.svg" />
  <img width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" />
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
 |    |    ├── 📁 core services     core servies responsible for business logic
 |    |    ├── 📁 postgre service   postgres database service
 |    |    └── 📁 redis             redis database service (currently disabled)
 |    ├── 📁 utils                  shared helper functions
 |    ├── 📝 main.py                backend entry point
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore
 |    ├── 🐳 Containerfile          backend container build
 |    └── 📝 pyproject.toml         python dependencies & config
 ├── 📁 frontend                    client-side application (development has not started)
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    ├── 📁 constants              global constants & configurations
 |    ├── 📁 hooks                  custom state & lifecycle hooks
 |    ├── 📝 package.json           frontend dependencies & scripts
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore
 |    └── 🐳 Containerfile          frontend container build
 ├── 🐳 compose.yaml                docker compose orchestration
 ├── 📄LICENCE                      LICENCE
 └── 📍README.md                    project description
```

## Run

To run the application, follow these steps:

**Copy the repository:**

```bash
git clone https://github.com/cyjiky/Clockly.git
```

**Move to repository directory:**

```bash
cd Clockly
```

### Using Docker Compose

**Run `compose.yaml`**

```bash
docker compose up
```

### Manually

#### Backend

Navigate to the repository directory

```bash
cd backend
```

Create virtual environment (recommended):

```bash
python -m venv ./venv
./venv/Scripts/activate

# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```

Install the dependencies:

```bash
pip install -e .
```

Setup PgAdmin with credentials specified in `.env` or run docker postgre image:

```bash
docker run --name clockly_postgres_container -e POSTGRES_USER=[USER] -e POSTGRES_PASSWORD=[PASSWORD] -e POSTGRES_DB=[DATABASE] -p 5432:5432 -d clockly-backend-postgres
```

Run the app

```bash
uvicorn main:app --reload
```

#### Frontend

Navigate to the repository root directory and then navigate to the frontend directory:

```bash
cd frontend
```

Install the dependencies:

```bash
npm i # or yarn install
```

Start the application via expo

```bash
npx expo start # or yarn expo start
```

## How to use FastAPI

https://fastapi.tiangolo.com

FastAPI provides automatic interactive documentation.

1. Ensure the backend server is running
2. Open your browser and navigate to: http://127.0.0.1:8000/docs (Swagger UI)
3. Here you can see all available endpoints and test requests directly in the browser

## Project status 
The project is currently under development

---

<div align="display:flex; gap:10px; align-items:center;">

**Authors**  
[@cyjiky](https://github.com/cyjiky) $\cdot$ [@yeghor](https://github.com/yeghor)

</div>
