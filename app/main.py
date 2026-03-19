from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.routes import router
from app.utils.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse


app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "Trade Opportunities API is running",
        "usage": "/analyze/{sector}",
        "docs": "/docs"
    }


app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

app.include_router(router)
