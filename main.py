from backend.run_server import app

if __name__ == "__main__":
    import uvicorn
    from database.db_create import Database

    # Создаем таблицу при запуске приложения
    Database().create_table()

    # Запуск сервера с использованием библиотеки uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
