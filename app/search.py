import feedparser
from urllib.parse import quote_plus

GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"

QUERY_MAP = {
    "jobs": '(AI creator OR "AI content creator" OR "AI video creator" OR "generative AI creator" OR "prompt engineer") (job OR vacancy OR hiring) (Kazakhstan OR Astana OR remote)',
    "projects": '("AI video" OR "AI animation" OR "Midjourney" OR "Kling" OR "Veo" OR "Runway") (freelance OR project OR contractor OR hiring)',
    "remote": '("AI creator" OR "AI video creator" OR "generative AI artist" OR "creative technologist") remote job',
    "cartoons": '("AI animation" OR "AI cartoon" OR "AI filmmaker" OR "animated video") (job OR project OR freelance)',
    "grants": '("AI film festival" OR "AI art grant" OR "generative AI competition" OR "open call")',
    "top": '("AI creator" OR "AI video creator" OR "AI animation" OR "generative AI artist") (remote OR freelance OR hiring OR grant OR competition)',
}

KEYWORDS = [
    "ai", "creator", "video", "animation", "generative", "prompt",
    "artist", "remote", "freelance", "ugc", "content", "kling",
    "midjourney", "veo", "runway", "higgsfield", "seedance",
    "cartoon", "film", "designer", "creative", "grant", "open call"
]


def score_item(title: str, summary: str) -> int:
    text = f"{title} {summary}".lower()
    return sum(1 for word in KEYWORDS if word in text)


def search_opportunities(category: str, limit: int = 7):
    query = QUERY_MAP.get(category, QUERY_MAP["top"])
    url = GOOGLE_NEWS_RSS.format(query=quote_plus(query))

    feed = feedparser.parse(url)
    results = []
    seen = set()

    for entry in feed.entries:
        title = entry.get("title", "").strip()
        link = entry.get("link", "").strip()
        summary = entry.get("summary", "").strip()

        if not title or not link or link in seen:
            continue

        score = score_item(title, summary)
        if score < 1:
            continue

        seen.add(link)
        results.append({
            "title": title,
            "link": link,
            "summary": summary,
            "score": score,
            "published": entry.get("published", "")
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]
