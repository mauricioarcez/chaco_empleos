FROM python:3.11.5-alpine3.18

WORKDIR /app

RUN apk update \
    && pip install --upgrade pip

COPY ./utils/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

ENV DJANGO_SETTINGS_MODULE=chacoempleos.settings.local

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]