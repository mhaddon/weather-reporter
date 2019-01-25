FROM python:3.7.0-alpine3.8

COPY . /code

ENV CACHE_LOCATION="/tmp/cached-weather/"
ENV CACHE_INVALIDATION_PERIOD=900
ENV OPEN_WEATHER_MAPS_API_KEY="NO_API_KEY_SET"

RUN pip3 install requests termcolor

WORKDIR /code

ENTRYPOINT python3 main.py
