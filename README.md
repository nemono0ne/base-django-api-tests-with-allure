# Django API Тесты с Allure

Создал основу для тестирования API на Django с использованием библиотеки pytest и генерации отчетов с помощью Allure.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/NemoNo0ne/base-django-api-tests-with-allure.git
    cd base-django-api-tests-with-allure
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate   # для Windows
    source .venv/bin/activate  # для Linux/MacOS
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите миграции базы данных:
    ```bash
    python manage.py migrate
    ```

5. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Тестирование

1. Для запуска тестов с pytest:
    ```bash
    pytest
    ```

2. Для генерации отчета с Allure:
    - Запустите тесты с меткой для Allure:
      ```bash
      pytest --alluredir=allure-results
      ```
    - Для отображения отчета:
      ```bash
      allure serve allure-results
      ```

## Что тестируется

Проект включает тесты для API, реализующего CRUD-операции для задач:
1. **Создание задачи**:
    - Тестирует создание новой задачи через API.
    - Проверяет успешный ответ с кодом 201 и правильность данных.

2. **Получение задач**:
    - Проверяет получение списка задач с кодом ответа 200.
    - Проверяет, что задача, созданная в тесте, присутствует в списке.

3. **Обновление задачи**:
    - Тестирует обновление существующей задачи через API.
    - Проверяет успешный ответ с кодом 200 и правильность обновленных данных.

4. **Удаление задачи**:
    - Тестирует удаление задачи через API.
    - Проверяет успешный ответ с кодом 204 и отсутствие задачи в базе.

## Структура проекта

- `task_manager/` — директория с основной логикой проекта.
- `tasks/` — директория с моделями и представлениями для работы с задачами.
- `tests/` — тесты для API и моделей.
- `allure-results/` — директория для хранения результатов тестов Allure.

## Примечания

Для правильной работы с Allure необходимо установить Java (8 или выше). Подробнее об установке Allure можно прочитать на официальной [странице](https://allure.qatools.ru/).
