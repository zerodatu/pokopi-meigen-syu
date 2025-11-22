from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ここに動画IDを載せて追加
# IDの説明…https://www.youtube.com/watch?v=xxxxxxxxxとあるとしてxxx..の部分がIDとなります!
VIDEOS = [
    {
        "youtube_id": "DVxFkC6KV6Y",  # ← 動画ID
        "title": "【ゲスト大発表】#ぽんぽこ24 ついにタイムスケジュール解禁！！！！",
        "quote": "柴田理恵",
    },
    {
        "youtube_id": "77Cv6hfeAXo",
        "title": "【超巨大】噂の台湾チキンが食べたいので自作しました！！",
        "quote": "ウマッドMAX→（ホンマ）世紀末やで",
    },
    {
        "youtube_id": "d9BZRH1IZqY",
        "title": "【ドッキリ】スマブラ中に急に深刻な話したら勝てる説",
        "quote": "どういうスタンス？ ",
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

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request},
    )

