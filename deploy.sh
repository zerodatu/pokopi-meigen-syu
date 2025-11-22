#!/bin/sh
    uvicorn index:app --reload --port 8000 &
    pid=$!
    sleep 1  # 起動待ち、必要に応じて伸ばす
    xdg-open http://127.0.0.1:8000
    wait $pid