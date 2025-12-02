import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# videos.jsonから動画データを読み込む
with open("videos.json", "r", encoding="utf-8") as f:
    VIDEOS = json.load(f)


def youtube_thumb(video_id: str) -> str:
    return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"


def youtube_link(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


@app.get("/", response_class=HTMLResponse)
async def list_quotes(request: Request):
    # テンプレートに渡す用の整形
    items = []
    for v in VIDEOS:
        vid = v["youtube_id"]
        items.append(
            {
                "title": v["title"],
                "quote": v["quote"],
                "thumb_url": youtube_thumb(vid),
                "url": youtube_link(vid),
            }
        )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "videos": items,
        },
    )

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request},
    )
