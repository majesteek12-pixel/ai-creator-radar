# AI Creator Radar v0.1

Персональный Telegram-бот для поиска AI-вакансий, фриланс-проектов и возможностей для AI-креатора.

## Что уже есть

- Telegram Bot на Python
- Команды:
  - `/start`
  - `/jobs`
  - `/projects`
  - `/remote`
  - `/cartoons`
  - `/grants`
  - `/top`
- Базовый поиск через RSS Google News
- Готовность к запуску на Render
- Переменные окружения через `.env`

## Быстрый запуск локально

1. Установить Python 3.11+
2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать файл `.env` по примеру `.env.example`
4. Вставить свой токен Telegram-бота:

```bash
TELEGRAM_BOT_TOKEN=your_token_here
```

5. Запустить:

```bash
python main.py
```

## Запуск на Render

1. Создай новый Web Service на Render
2. Подключи GitHub-репозиторий
3. Build Command:

```bash
pip install -r requirements.txt
```

4. Start Command:

```bash
python main.py
```

5. В Environment Variables добавь:

```bash
TELEGRAM_BOT_TOKEN=твой_токен
```

Важно: токен не публиковать в GitHub и не отправлять в чаты.
