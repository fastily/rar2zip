"""Main module, contains logic for web app"""

import logging
import subprocess

from contextlib import asynccontextmanager
from pathlib import Path
from uuid import uuid4

import uvicorn

from aiofiles.tempfile import TemporaryDirectory, NamedTemporaryFile
from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from rich.logging import RichHandler

from .utils import Settings

_CHUNK_SIZE = 1024 * 1024 * 4

log = logging.getLogger(__name__)
log.addHandler(RichHandler(rich_tracebacks=True))
log.setLevel(logging.INFO)

OUT_DIR = Path(Settings().out_dir)


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Initialization and teardown code

    Args:
        _ (FastAPI): FastAPI object, not used.
    """
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    yield

app = FastAPI(title="Unrar Tool", docs_url=None, redoc_url=None, lifespan=lifespan)
templates = Jinja2Templates("unrar_tool/templates")


@app.get("/")
async def show_index(request: Request) -> HTMLResponse:
    """Shows the web UI"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def upload(f: UploadFile) -> dict[str, str]:
    """File upload endpoint.

    Args:
        f (UploadFile): The file that was uploaded

    Returns:
        dict: Some JSON indicating if the operation was successful.
    """
    if f.content_type in ("application/vnd.rar", "application/x-rar"):
        raise HTTPException(status_code=400, detail="File format not supported. Please upload a .rar file")

    async with TemporaryDirectory() as d, NamedTemporaryFile() as rar_file:
        while content := await f.read(_CHUNK_SIZE):
            await rar_file.write(content)
        await rar_file.flush()

        extract_dir = Path(d) / "extracted"
        output_zip = (OUT_DIR / str(uuid4())).with_suffix(".zip")

        if subprocess.run(f"unar -D -o '{extract_dir}' '{rar_file.name}' && zip -jr '{output_zip}' '{extract_dir}'", shell=True).returncode:
            raise HTTPException(status_code=500, detail="Unable extract files?")

        return FileResponse(output_zip, filename=Path(f.filename.replace("/", "_").replace(":", "-")).with_suffix(".zip").name)


if __name__ == '__main__':
    uvicorn.run("unrar_tool.__main__:app", reload=True)
