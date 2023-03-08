# project/app/main.py

import logging

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import get_settings, Settings

from app.api import ping
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    application.include_router(ping.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info('Starting up ...')
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down ...")

# @app.get("/ping")
# async def pong(settings: Settings = Depends(get_settings)):
#     return {"ping": "pongster!",
#             "environment": settings.environment,
#             "testing": settings.testing
#             }
