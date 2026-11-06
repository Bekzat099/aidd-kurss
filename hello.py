"""Приветствие с сегодняшней датой. Только стандартная библиотека."""
from datetime import date


def greet(name: str) -> str:
    """Собирает строку приветствия с датой в формате КК.АА.ГГГГ."""
    today = date.today()
    return f"Сәлем, {name}! Бүгін {today.day}.{today.month}.{today.year}"


def main() -> None:
    name = input("Атыңызды жазыңыз: ").strip() or "Достым"
    print(greet(name))


if __name__ == "__main__":
    main()
