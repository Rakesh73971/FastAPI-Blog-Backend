@echo off

echo Triggering FastAPI job...

curl -X POST http://127.0.0.1:8000/jobs/run ^
 -H "Content-Type: application/json" ^
 -d "{\"task\":\"nightly_job\"}"



echo.
curl -X GET http://127.0.0.1:8000/jobs/status

pause
