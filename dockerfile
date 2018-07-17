FROM tiangolo/uwsgi-nginx-flask:python3.6

LABEL maintainer="usagikeri <a.k.a.usagikeri@gmail.com>"

RUN pip install bibtexparser
COPY ./app /app

