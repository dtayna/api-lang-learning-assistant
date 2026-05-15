# Backend - Lang Learning Assistant

## 1

```bash
git clone https://github.com/dtayna/api-lang-learning-assistant
cd api-lang-learning-assistant
```

---

## 2

```bash
python -m venv venv
```
And... Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3

```bash
pip install -r requirements.txt
```

---

## 4

Create`.env` in the root:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_DB=lang_learning

DATABASE_URL=postgresql://postgres:1234@localhost:5432/lang_learning
```

---

## 5

```bash
docker compose up -d
```

---

## 6. Run API

```bash
uvicorn app.main:app --reload
```

---

## 7 

API:

```txt
http://localhost:8000
```

Swagger:

```txt
http://localhost:8000/docs
```

---

## To stop container or remove all data

```bash
docker compose down
```

```bash
docker compose down -v
```