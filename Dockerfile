FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/entries

COPY requirements.txt .
COPY . .

pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "/manage.py"]
