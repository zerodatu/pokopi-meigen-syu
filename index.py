from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 🔽 ここにあなた様が推しVTuberの動画リストを追加していく
VIDEOS = [
    {
        "youtube_id": "dQw4w9WgXcQ",  # ← 動画ID
        "title": "【雑談】〇〇について語る配信",
        "quote": "あきらめた瞬間に、夢はそこで終わっちゃうんだよ",
    },
    {
        "youtube_id": "XXXXXXXXXXX",
        "title": "【歌枠】〇〇歌ってみた",
        "quote": "今日のあなたが、いちばんかわいい日だよ",
    },
    # 追加していけばどんどん増える
]


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
