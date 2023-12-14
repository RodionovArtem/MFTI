from fastapi import FastAPI
from fastapi.responses import JSONResponse
from parser import get_product_info
from database.db_create import Database

app = FastAPI()
db = Database()  # Создаём экземпляр класса Database


@app.get('/')
async def read_root():
    db.clear_data()  # Вызываем метод clear_data, для удаления данных из базы данных
    get_product_info()  # Вызываем метод get_ingo_product для парсинга информации о товарах

    #  При завершении парсинг выводим сообщение в виде JSON строки
    return JSONResponse(content={'message': 'Парсинг данных успешно завершился, все данные добавлены в базу данных.'})



