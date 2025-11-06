@echo off
call .\venv\Scripts\activate
uvicorn main:app --reload --port 8001
pause


git init
git add .
git commit -m "Initial commit: PDN Calculator project ready for deploy"
git branch -M main
git remote add origin https://github.com/YuriyNik156/pdn-calculator-new.git
git push -u origin main
