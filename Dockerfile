FROM python

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY unrar_tool ./unrar_tool
COPY requirements.txt .

RUN apt-get update && apt-get install -y unar && apt-get clean && rm -rf /var/cache/apt/lists && \
    python -m venv venv_unrar_tool && . venv_unrar_tool/bin/activate && pip install -r requirements.txt && deactivate

ENTRYPOINT ["./venv_unrar_tool/bin/gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "unrar_tool.__main__:app"]