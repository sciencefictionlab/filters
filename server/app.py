from pprint import pprint
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse, RedirectResponse

from server.singletons.config import AppConfig
from server.routes.image_filter import router as image_router

config = AppConfig.get_config()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def catchall_exception_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        pprint(e)
        return JSONResponse({'detail': '"Internal server error"'}, status_code=500)


if config.APP_ENV == 'prod':
    app.middleware('http')(catchall_exception_middleware)


app.include_router(image_router, prefix='/image', tags=["image-filters operations"])


@app.get('/', response_description="fetch company details")
async def _r():
    return RedirectResponse('/arbiter')
