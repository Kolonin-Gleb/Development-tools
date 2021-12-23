FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements requirements
RUN pip3 install -r requirements
COPY .. .
EXPOSE 80
CMD [ "python3", "web_site_logs.py"]