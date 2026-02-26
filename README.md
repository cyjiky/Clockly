# Clockly 

### Stack

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

---

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

Move to backend application directory
```bash
cd backend
```

Create virtual envronment (recommended):
```bash
python -m venv ./venv
./venv/Scripts/activate
```

Install the dependencies
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

Move to the repository root directory and then navigate to the frontend directory:
```bash
cd frontend
```

Install the dependendies:
```bash
npm i # or yarn install
```

Start the application via expo
```bash
npx expo start # or yarn expo start
```

---

<div align="display:flex; gap:10px; align-items:center;">

**Authors**  
[@cyjiky](https://github.com/cyjiky) $\cdot$ [@yeghor](https://github.com/yeghor)

</div>
