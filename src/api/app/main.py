
from fastapi import FastAPI


from app.core.config import envSettings
from app.events.router import router as events_router
from app.attendees.router import router as attendees_router
from app.auth.router import router as auth_router
from app.users.router import router as users_router

from app.auth.api_key_authentication import api_key_dependency


app_configs = {
    "title": "Event Quill API",
    "description": "API for Event Quill",
    "version": "0.0.1",
    "summary": "API for Event Quill",
    "redoc_url": "/documentation",

}

SHOW_DOCS_ENVIRONMENT = ("development", "staging")
if envSettings.ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["docs_url"] = None


app = FastAPI(**app_configs)

app.include_router(events_router, prefix="/v1")
app.include_router(attendees_router, prefix="/v1")
app.include_router(auth_router, prefix="/v1")
app.include_router(users_router, prefix="/v1")
