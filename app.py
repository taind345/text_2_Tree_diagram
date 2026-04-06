from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tree_logic import parse_indented_text, format_tree
import os
import sys
import threading
import uvicorn
import webview

# Helper to get base path for templates (works for PyInstaller bundling)
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

app = FastAPI()

# Setup templates
templates_dir = get_resource_path("templates")
templates = Jinja2Templates(directory=templates_dir)

class TreeRequest(BaseModel):
    text: str
    spaces: int = 2

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/convert")
async def convert_text(req: TreeRequest):
    parsed = parse_indented_text(req.text, spaces_per_level=req.spaces)
    tree_str = format_tree(parsed)
    return {"tree": tree_str}

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

if __name__ == "__main__":
    # Start FastAPI server in a background thread
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    
    # Create a webview window
    webview.create_window('Text2Tree Converter', 'http://127.0.0.1:8000', 
                          width=1100, height=800, 
                          min_size=(800, 600))
    webview.start()
