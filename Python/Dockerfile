FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --cache-dir=/root/.cache/pip -r requirements.txt

COPY seeds_creation.py .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV DBT_PROFILES_DIR=../dbtlearn

CMD ["/entrypoint.sh"]


