FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip
COPY requirements.txt /code/

RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
