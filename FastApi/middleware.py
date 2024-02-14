from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
import logging

# Create a FastAPI application
app = FastAPI()

# Define a custom middleware class
class LoggingMiddleware(BaseHTTPMiddleware):
    async def __call__(self, request, call_next):
        # Log information about the incoming request
        logging.info(f"Received request: {request.method} {request.url}")
        
        # Continue processing the request
        response = await call_next(request)
        
        # Log information about the outgoing response
        logging.info(f"Sent response: {response.status_code}")
        
        return response

# Add the custom middleware to the FastAPI application
app.add_middleware(LoggingMiddleware)

# Define a sample route
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
