# Stellar Burgers UI Tests

UI-тесты для веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru/).


## Структура проекта
```
Task_3/
├── pages/ # Page Object классы
├── locators/ # Локаторы элементов
├── utils/ # Утилиты (API, генераторы, URLs)
├── tests/ # Тесты
└── allure-results/ # Результаты Allure
└──conftest.py # Фикстуры 
```

## Установка

```
pip install -r requirements.txt
```

## Запуск тестов

# Все тесты в Chrome
```
pytest tests/ --browser=chrome -v
```

# Все тесты в Firefox
```
pytest tests/ --browser=firefox -v
```

## Кроссбраузерность
Тесты запускаются в Chrome и Firefox через фабрику браузеров# Task_3
