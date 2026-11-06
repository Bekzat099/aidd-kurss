# aidd

AI-Driven Development курса — 1-апта, 2-сабақ: алғашқы Python-скрипт, Git және GitHub.

## Не істейді

`hello.py` атыңды сұрап, бүгінгі күнмен (КК.АА.ЖЖЖЖ форматында) сәлемдеседі:

```text
Атыңызды жазыңыз: Әли
Сәлем, Әли! Бүгін 6.11.2026
```

## Қалай іске қосу керек

```bash
# 1. виртуалды орта (бір рет)
python -m venv .venv

# 2. ортаны қосу
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# 3. скрипт
python hello.py
```

## Курстың Git тәртібі

- бір тармақ — бір тапсырма: `feature/...`
- тармақ → коммит → push → Pull request → merge
- құпиялар репозиторийге түспейді: `.env`, `.venv/` — `.gitignore`-да
