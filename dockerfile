FROM python:3.6

LABEL maintainer="usagikeri <a.k.a.usagikeri@gmail.com>"

RUN pip install flask   \
        bibtexparser

WORKDIR /home
COPY src .

EXPOSE 80

CMD ["python3 app.py"]
