import os, sys, threading, uvicorn, webview
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tree_logic import parse_indented_text, format_tree

app = FastAPI()

def get_path(path):
    base = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base, path)

templates = Jinja2Templates(directory=get_path("templates"))

class TreeRequest(BaseModel):
    text: str
    spaces: int = 2

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/convert")
async def convert(req: TreeRequest):
    nodes = parse_indented_text(req.text, req.spaces)
    return {"tree": format_tree(nodes)}

if __name__ == "__main__":
    threading.Thread(target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error"), daemon=True).start()
    webview.create_window('Text2Tree', 'http://127.0.0.1:8000', width=1100, height=850)
    webview.start()
