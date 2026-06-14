import json
from pathlib import Path


# Хранение сессий в памяти: {user_id: {"track": [...], "step": 0, "mask": "..."}}
_sessions: dict = {}


def load_track(track_name: str) -> list:
    """Загружает трек из JSON-файла."""
    path = Path("tracks") / f"{track_name}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_mask(mask_name: str) -> str:
    """Загружает системный промпт маски наставника."""
    path = Path("masks") / f"{mask_name}.txt"
    return path.read_text(encoding="utf-8")


def start_session(user_id: int, track_name: str, mask_name: str) -> str:
    """Начинает новую сессию и возвращает первый вопрос трека."""
    track = load_track(track_name)
    mask = load_mask(mask_name)
    _sessions[user_id] = {"track": track, "step": 0, "mask": mask}
    return track[0]["question"]


def next_step(user_id: int) -> str | None:
    """Переходит к следующему шагу. Возвращает вопрос или None если трек завершён."""
    session = _sessions.get(user_id)
    if not session:
        return None
    session["step"] += 1
    if session["step"] >= len(session["track"]):
        del _sessions[user_id]
        return None
    return session["track"][session["step"]]["question"]


def get_mask(user_id: int) -> str | None:
    """Возвращает системный промпт текущей маски пользователя."""
    session = _sessions.get(user_id)
    return session["mask"] if session else None


def has_session(user_id: int) -> bool:
    return user_id in _sessions
