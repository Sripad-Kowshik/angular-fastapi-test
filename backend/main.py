# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- CORS Configuration ---
# This is crucial to allow your Angular app (running on a different port)
# to communicate with the FastAPI backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# --- End CORS Configuration ---

@app.get("/")
async def read_root():
    """
    Root GET endpoint that returns a simple message.
    """
    return {"message": "Hello from FastAPI! 👋"}

@app.get("/api/data")
async def get_data():
    """
    Another example endpoint.
    """
    return {"content": "This is some data served from /api/data"}

# To run the app (from the 'backend' directory):
# uvicorn main:app --reload
