# Автотесты с использованием Pytest и Selenium

Проект содержит автотесты для веб-приложения https://stellarburgers.nomoreparties.site/
с использованием Pytest и Selenium с целью проверки базового функционала 

## Установка

1. Склонируйте репозиторий

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate Для Windows используйте venv\Scripts\activate

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

## Запуск тестов

1. Убедитесь, что виртуальное окружение активировано.
2. Запустите тесты с использованием pytest:
   ```bash
   pytest или pytest -n auto

## Allure и генерация отчетов

1. Для генерации отчетов Allure используйте:
   ```bash
   pytest --alluredir=allure_results
2. Убедитесь, что у вас установлен Allure CLI.
3. После запуска тестов с флагом --alluredir, выполните следующую команду для генерации отчетов:
   ```bash
   allure serve allure_results