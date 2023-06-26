from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse



class Item(BaseModel):
    prompt: str
    image_base64: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="dist"), name="static")


@app.get("/")
def root():
    # Redirect to the index.html in the static directory
    return RedirectResponse(url="/static/index.html")

@app.post("/transform_image")
async def transform_image(item: Item):
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

@app.get("/{path:path}")
def redirect_to_static(path: str):
    # Exclude the "/transform_image" endpoint from redirection
    if path == "transform_image":
        raise HTTPException(status_code=404, detail="Not Found")
    return RedirectResponse(url=f"/static/{path}")
