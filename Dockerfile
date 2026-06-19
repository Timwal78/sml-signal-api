FROM python:3.12-slim
WORKDIR /app

# Prevent glibc memory fragmentation (OOM Fix)
ENV MALLOC_ARENA_MAX=2
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8010
CMD ["sh", "-c", "python mcp_server_sml.py"]
