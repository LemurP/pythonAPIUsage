FROM python:rc-alpine

RUN apk add -u --no-cache python3 \
    #&& apk add -u --no-cache --virtual .build-deps build-base g++ libffi-dev curl-dev \
    && pip install --no-cache-dir requests pytest \
    #&& apk del --no-cache --purge .build-deps \
    && rm -rf /var/cache/apk/*

VOLUME src /myvol/src
VOLUME tests /myvol/tests