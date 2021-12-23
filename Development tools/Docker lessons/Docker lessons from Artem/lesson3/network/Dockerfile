FROM python:3.7-alpine
WORKDIR /app
COPY requirements requirements
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install psycopg2-binary
RUN pip3 install -r requirements
COPY .. .
EXPOSE 80
CMD [ "python3", "network.py"]