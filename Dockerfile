FROM python:slim

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app
COPY rar2zip ./rar2zip
COPY requirements.txt .

RUN apt-get update && apt-get install -y unar zip && apt-get clean && rm -rf /var/cache/apt/lists && \
    python -m venv venv_rar2zip && . venv_rar2zip/bin/activate && pip install --no-cache-dir -r requirements.txt && deactivate

ENTRYPOINT ["./venv_rar2zip/bin/gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "rar2zip.__main__:app"]