FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/entries

COPY requirements.txt .
COPY . .
COPY manage.py ./

RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000

CMD ["python", "./manage.py", "runserver"]
