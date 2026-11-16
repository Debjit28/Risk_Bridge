FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project for uv to detect the package structure
COPY . .

RUN pip install --no-cache-dir uv \
    && uv sync --frozen --no-dev

EXPOSE 8000

ENV PYTHONPATH=/app/src

CMD ["uv", "run", "uvicorn", "backend.main:app", \
     "--host", "0.0.0.0", "--port", "8000"]