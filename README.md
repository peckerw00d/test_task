# Установка и запуск

## 1. Клонирование репозитория

```bash
git clone https://github.com/peckerw00d/test_task
cd test_task
```

## 2. Сборка и запуск Docker-контейнера

```bash
make setup
```

Приложение будет доступно по адресу:

```
http://localhost:8000
```

## 3. Запуск тестового скрипта

```bash
python test_script.py
```

Сервер должен вернуть следующее:

```
GET FORM Response: MyForm
```