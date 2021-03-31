FROM python:3
ENV PYTHONUNBUFFERED=
ENV TZ 'US/Eastern'
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/