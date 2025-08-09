# rar2zip
[![Python 3.12+](https://upload.wikimedia.org/wikipedia/commons/5/50/Blue_Python_3.12%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

A simple web service that makes it easy to convert rar to zip

⚠️ Do not run this in an untrusted environemnt, the app assumes any input files are safe.

## Dependencies
* [unar](https://theunarchiver.com/command-line)

## Usage
```bash
# install dependencies
uv sync --no-install-project

# start in development mode, visit http://127.0.0.1:8000 to view the web interface
uv run python -m rar2zip

# run w/ gunicorn, accessible at localhost:8000
uv run gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b "0.0.0.0" rar2zip.__main__:app
```