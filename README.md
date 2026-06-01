# ashan

Краткое описание проекта. 

Веб-приложение на Django для продажи товаров онлайн

---

## Возможности

- выбори и заказ товара 
- Админ панель Django
- Загрузка файлов и изображений


## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Daren-art/ashan.git
cd project
```

### 2. Создать виртуальное окружение

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r req.txt
```

---

## Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Создание суперпользователя (админ)

```bash
python manage.py createsuperuser
```

---

## Запуск проекта

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
