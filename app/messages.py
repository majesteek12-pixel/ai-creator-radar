import re
from html import unescape


def clean_text(text: str, max_len: int = 220) -> str:
    text = unescape(text or "")
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`\[\]]", "", text)
    text = " ".join(text.split())
    if len(text) > max_len:
        text = text[:max_len].rstrip() + "..."
    return text


def welcome_message() -> str:
    return (
        "*AI Creator Radar v0.1*\n\n"
        "Я ищу вакансии, фриланс-проекты и возможности для AI-креатора.\n\n"
        "*Команды:*\n"
        "/jobs — AI-вакансии\n"
        "/projects — фриланс-проекты\n"
        "/remote — удалённая работа\n"
        "/cartoons — мультфильмы и AI-анимация\n"
        "/grants — гранты и конкурсы\n"
        "/top — лучшие возможности дня\n\n"
        "Приоритет: Астана, Казахстан, remote, AI-видео, мультфильмы, UGC, бренды."
    )


def help_message() -> str:
    return welcome_message()


def format_opportunities(title: str, items: list) -> str:
    if not items:
        return (
            f"*{title}*\n\n"
            "Пока не нашла достаточно релевантных предложений. Попробуй позже."
        )

    msg = f"*{title}*\n\n"
    for i, item in enumerate(items, 1):
        item_title = clean_text(item.get("title", ""), 120)
        summary = clean_text(item.get("summary", ""), 180)
        link = item.get("link", "")
        score = item.get("score", 0)

        msg += f"*{i}. {item_title}*\n"
        msg += f"Score: {score}/20\n"
        if summary:
            msg += f"{summary}\n"
        msg += f"{link}\n\n"

    msg += "Фильтр: AI Creator / AI Video / Animation / Remote / Kazakhstan / Freelance."
    return msg
