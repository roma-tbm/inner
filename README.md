# INNER

**INNER** — интерактивный ИИ-наставник в формате структурированных сессий.

Это не планировщик задач, не коуч и не чат-бот для ответов на вопросы.

INNER помогает человеку слышать собственный голос сквозь шум внешнего мира — через осмысленный диалог, где ИИ не отвечает, а задаёт вопросы.

---

## Концепция

Обычный чат-бот: `Пользователь → Вопрос → Ответ`

INNER: `ИИ → Вопрос → Осознание → Новый вопрос → Изменение`

Пользователь проходит заранее спроектированные сценарии («треки»), выбирая голос наставника («маску»).

---

## Треки

| Файл | Описание |
|---|---|
| `ya_zastryal.json` | Для ситуаций, когда непонятно куда двигаться |
| `nado_reshitsya.json` | Для принятия сложного решения |

---

## Маски наставников

| Файл | Стиль |
|---|---|
| `streetwise.txt` | Прямой, честный, говорит как старший брат |
| `wise_woman.txt` | Мягкость, принятие, эмоциональная глубина |

---

## Стек

- Python 3.11+
- python-telegram-bot
- DeepSeek API
- JSON (сценарии треков)

---

## Установка

```bash
git clone https://github.com/your-username/inner.git
cd inner
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# заполни .env своими ключами
python inner_bot.py
```

---

## Структура проекта

```
inner/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── inner_bot.py
├── deepseek_api.py
├── tracks/
│   ├── ya_zastryal.json
│   └── nado_reshitsya.json
├── masks/
│   ├── streetwise.txt
│   └── wise_woman.txt
└── utils/
    └── session_manager.py
```

---

## Критерий успеха MVP

После сессии пользователь говорит:

> «Это заставило меня задуматься.»

или

> «Я увидел что-то важное про себя.»

---

## Принцип

Сначала опыт. Потом форма. Потом технология.
