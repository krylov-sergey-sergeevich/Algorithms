# Реализация алгоритмов на Python

## Оглавление

### Арифметика

1. [Факторизация числа (разложение на множители)](src/arithmetic/factor.py)

## Настройка проекта

1. **Клонирование проекта**

`git clone https://github.com/krylov-sergey-sergeevich/Algorithms.git`

2. **Установка зависимостей**

- `pip install -e .`
- `pip install -r .\requirements_dev.txt`

### Команды проверки кода и тестов

- `tox` - _включает в себя нижеописанные_
    - `mypy src` - _проверяет что код соответствует логики (по типам и т.д.)_
    - `flake8 src` - _проверяет стиль написания_
    - `pytest` - _прогоняет тесты_