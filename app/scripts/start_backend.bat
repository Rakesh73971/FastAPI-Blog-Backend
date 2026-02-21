@echo off
cd /d C:\path\to\your\project
call venv\Scripts\activate
uvicorn app.main:app 
