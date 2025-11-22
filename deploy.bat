@echo off
rem uvicornサーバーを起動します。
rem --reloadオプションを付けているため、コードの変更が自動で反映されます。
start "uvicorn" uvicorn index:app --reload --port 8000

rem サーバーが起動するのを少し待ちます（ここでは2秒）。環境に応じて調整してください。
timeout /t 2 /nobreak > nul

rem デフォルトのブラウザで http://127.0.0.1:8000 を開きます。
start http://127.0.0.1:8000

