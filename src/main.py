from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
middleware = [
    Middleware(
        TrustedHostMiddleware,
        allowed_hosts=['localhost:4200'],
    ),
    Middleware(CORSMiddleware, allow_origins=['*']),
    Middleware(HTTPSRedirectMiddleware)
]

app = Starlette(middleware=middleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}
