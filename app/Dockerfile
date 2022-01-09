FROM python:3.7-alpine

WORKDIR /backend

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY catbase/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY catbase .
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
