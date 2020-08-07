FROM python:3.8

EXPOSE 8080

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/

ENTRYPOINT ["/app/entrypoint.sh"]

CMD python run.py
