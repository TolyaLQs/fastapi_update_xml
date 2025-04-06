# main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import engine, SessionLocal
import models
from routers import files, admin
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from contextlib import asynccontextmanager
import os

models.Base.metadata.create_all(bind=engine)

# Email configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "user@example.com"
SMTP_PASSWORD = "password"
ADMIN_EMAIL = "admin@example.com"

# Scheduler
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(files.router)
app.include_router(admin.router)


def send_email(subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ADMIN_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)


async def parse_file_job(site_id):
    try:
        db = SessionLocal()
        latest_file = db.query(models.Site).order_by(models.Site.id.desc()).first()
        if not latest_file:
            return

        # Пример обработки файла
        input_path = os.path.join("uploads", latest_file.filename)
        output_path = os.path.join("output", f"processed_{latest_file.filename}")

        # Здесь должна быть логика обработки файла
        with open(input_path, "r") as f_in, open(output_path, "w") as f_out:
            content = f_in.read()
            f_out.write(content.upper())

        stats = f"File processed: {os.path.getsize(output_path)} bytes"
        send_email("Parsing Success", stats)
    except Exception as e:
        send_email("Parsing Error", str(e))
    finally:
        db.close()


@app.on_event("startup")
async def schedule_jobs():
    db = SessionLocal()
    try:
        timemarks = db.query(models.TimeMark).all()
        if timemarks:
            for tm in timemarks:
                scheduler.add_job(
                    parse_file_job(tm.site_id),
                    'cron',
                    day_of_week=tm.day_of_week,
                    hour=tm.hour,
                    minute=tm.minute,
                    id=f"timemark_{tm.id}"
                )
    except:
        print("Failed to schedule jobs")
    finally:
        db.close()


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/admin")
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@app.get("/admin/site/{site_id}")
async def admin_site(request: Request, site_id: int):
    return templates.TemplateResponse("site.html", {"request": request, 'site_id': site_id})


if __name__ == "__main__":
    import uvicorn
    # Запуск сервера
    uvicorn.run(app, host="0.0.0.0", port=8000)


