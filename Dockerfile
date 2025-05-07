FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-dev build-essential

ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install virtualenv && virtualenv $VIRTUAL_ENV

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install Pillow

COPY . /srv/app

RUN chmod -R 777 /srv/app

WORKDIR /srv/app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

