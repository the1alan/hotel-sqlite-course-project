# Курсовой проект: «Проектирование базы данных для гостиницы»

Минимальный учебный проект на Flask + SQLite с одной веб-страницей.

## Что реализовано
- Flask-приложение с отображением:
  - статистики,
  - номеров,
  - гостей,
  - бронирований,
  - услуг,
  - платежей.
- Две формы:
  - добавление гостя,
  - добавление бронирования.
- SQLite-схема с внешними ключами, CHECK-ограничениями и тестовыми данными.

## Структура
- `app.py` — основной Flask-сервер.
- `init_db.py` — инициализация базы данных из SQL-файлов.
- `sql/01_create_tables.sql` — создание таблиц.
- `sql/02_insert_data.sql` — тестовые данные.
- `sql/03_queries.sql` — примеры SQL-запросов.
- `templates/index.html` — страница интерфейса.
- `static/style.css` — стили.
- `static/script.js` — клиентская валидация формы.

## Запуск
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
python app.py
```

Откройте в браузере: `http://localhost:5000`
