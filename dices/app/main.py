from fastapi import FastAPI

from app.controllers import roll_router
from app.config import logger, API_PREFIX

app = FastAPI()

app.include_router(roll_router, prefix=API_PREFIX)
