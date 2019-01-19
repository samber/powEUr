
FROM python:3

ENV PYTHONBUFFERED=0 \
    PYTHONUNBUFFERED=1 \
    PACKAGES=cron

WORKDIR /usr/src/app
# CMD python3 crawler-today.py
CMD cron -f

RUN apt-get update \
    && apt-get -y --no-install-recommends install ${PACKAGES} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY crontab /tmp/crontab
RUN cat /tmp/crontab | crontab -

COPY . /usr/src/app/

RUN pip3 install -r requirements.txt
