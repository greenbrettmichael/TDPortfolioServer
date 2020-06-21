FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]