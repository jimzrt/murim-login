FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git \
    && rm -rf /var/lib/apt/lists/*

ENV PI_INSTALL_DIR=/usr/local/bin
RUN curl -fsSL https://omp.sh/install | sh -s -- --binary \
    && omp --version

COPY docker/report/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY tools /app/tools
COPY .omp /app/.omp
ENV PYTHONUNBUFFERED=1
ENV MURIM_ROOT=/app
ENV REPORT_HOST=0.0.0.0
ENV REPORT_PORT=8080
ENV HOME=/root
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"

CMD ["python", "-m", "tools.report_server"]
