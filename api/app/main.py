from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from logger import logger
from config import load_config
from models import User

app = FastAPI()
config = load_config()

external_data = {
    "id": "123",
    "name": "Rolya",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)

@app.get('/')

async def index():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return FileResponse('index.html')

@app.post('/calculate')

async def calc(num1:int = Form(), num2:int = Form()):

    return {'result': num1+num2}

@app.get('/users')
async def users():
    return user.id, user.name



if config.debug:
    app.debug = True
else:
    app.debug = False


# uvicorn main:app --reload   - Запуск файла где app это переменная в которую помещен FastApi ее можно назвать как угодно
# fastapi dev или run main.py   - Тоже запуск
# Мы будем использовать библиотеку environs, которая помогает загружать переменные окружения из файла .env и выполнять валидацию 
# типов данных. Это современная альтернатива python-dotenv.