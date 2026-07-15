# Test Framework

Автотесты для веб-приложения (Playwright + pytest) и REST API (httpx + pydantic). Отчёты — Allure.

## Стек

- Python 3.12+
- pytest, pytest-playwright, playwright
- httpx, pydantic, pydantic-settings
- allure-pytest, Faker

## Что нужно до запуска

1. Работающее приложение под тест (URL в `.env` должен совпадать с реальным адресом фронта и API).
2. Учётные данные тестового пользователя и администратора (см. переменные окружения ниже).

## Быстрый старт

```bash
git clone https://github.com/DmitVar/test-framework.git
cd test-framework

python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
playwright install
```

Создайте файл `.env` в корне репозитория (шаблон ниже). Без него настройки из `config.py` не поднимутся

## Переменные окружения (`.env`)

Используется `pydantic-settings`; для вложенных полей — двойное подчёркивание `__`.

Пример (подставьте свои значения):

```env
# URL фронта (для UI)
APP_URL=http://localhost:3000

# Браузер: chromium | firefox | webkit
BROWSER=["chromium"]

HEADLESS=false

# REST API (базовый URL бэкенда)
HTTP_CLIENT__URL=http://localhost:8000
HTTP_CLIENT__TIMEOUT=30.0

# Тестовый пользователь
TEST_USER__EMAIL=user@example.com
TEST_USER__PASSWORD=your_password
TEST_USER__USERNAME=user

# Администратор
TEST_ADMIN__EMAIL=admin@example.com
TEST_ADMIN__PASSWORD=your_admin_password
TEST_ADMIN__USERNAME=admin
```

При необходимости добавьте другие поля, которые ожидает ваш `Settings` в `config.py`.

Для UI-фикстур с сохранённой сессией каталог `.auth/` создаётся автоматически (см. `fixtures/web_ui/ui_auth_fixtures.py`); его не коммитьте.

## Запуск тестов

По умолчанию в `pytest.ini` включены подробный вывод, браузер Chromium, **headed**-режим, скриншоты и видео при падениях, каталог Allure `allure-results`.

```bash
# все тесты
pytest

# только API
pytest -m "api"

# только UI
pytest -m "ui"

# дымовой набор
pytest -m "smoke"

# регрессия
pytest -m "regression"

# сочетания
pytest -m "api and smoke"
```

### Маркеры (`pytest.ini`)

| Маркер            | Назначение                          |
|-------------------|-------------------------------------|
| `api`             | тесты REST API                      |
| `ui`              | тесты через браузер                |
| `smoke`           | короткий критичный набор           |
| `regression`      | расширенные сценарии               |
| `authorization` | авторизация / доступ к защищённым  |
| `registration`    | регистрация и связанные сценарии   |

Незарегистрированные маркеры дают предупреждение Pytest — добавляйте новые в `pytest.ini`, если вводите свои.

### Только API в CI

Если не нужен браузер:

```bash
pytest -m "api"
```

## Allure

Результаты пишутся в каталог `allure-results` (очищается при запуске из-за `--clean-alluredir` в `pytest.ini`).

Просмотр отчёта (нужен [Allure Commandline](https://github.com/allure-framework/allure2)):

```bash
allure serve allure-results
```

## Форматирование кода

В `pyproject.toml` настроены Black и isort (цель — Python 3.12).

```bash
black .
isort .
```

## Структура проекта

```
test-framework/
├── config.py              # настройки (pydantic-settings, .env)
├── conftest.py            # плагины pytest, хуки Allure
├── pytest.ini             # pytest, маркеры, опции Playwright/Allure
├── requirements.txt       # зависимости
├── core/
│   ├── api/clients/       # HTTP-клиенты и схемы API
│   └── web_ui/            # Page Object, компоненты, элементы
├── fixtures/              # фикстуры API и UI
├── tests/
│   ├── api/               # тесты API (users, authentication, boards, …)
│   └── web_ui/            # тесты UI
└── tools/                 # ассерты, логирование, Allure-утилиты
```

Сгенерированные артефакты (`allure-results/`, `video/`, `tracing/` и т.д.) указаны в `.gitignore` — не коммитьте их в репозиторий.

## Лицензия и автор

Пет-проект / дипломный проект. При публикации укажите свою лицензию или оставьте как есть в учебных целях.
