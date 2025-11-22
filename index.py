from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ここに動画IDを載せて追加
# IDの説明…https://www.youtube.com/watch?v=xxxxxxxxxとあるとしてxxx..の部分がIDとなります!
VIDEOS = [
    {
        "youtube_id": "dQw4w9WgXcQ",  # ← 動画ID
        "title": "【雑談】〇〇について語る配信",
        "quote": "あきらめた瞬間に、夢はそこで終わっちゃうんだよ",
    },
    {
        "youtube_id": "77Cv6hfeAXo",
        "title": "【超巨大】噂の台湾チキンが食べたいので自作しました！！",
        "quote": "ウマッドMAX→（ホンマ）世紀末やで",
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
