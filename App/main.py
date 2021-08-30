from typing import Optional, Any
from fastapi import FastAPI

import uvicorn

from send import send_message
from config import settings
    

app = FastAPI(title='Send email')


@app.get("/")
def index():
    return {"hello": "world"}


@app.post("/contact")
async def contact():
    try:
        await send_message("example@example.com", "example_subject", "example_message")
        return True
    except Exception:
        return False
    
        
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True) # host & port can be set in config file
