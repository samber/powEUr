
FROM python:3.7

ENV PYTHONBUFFERED=0 \
    PYTHONUNBUFFERED=1 \
    PACKAGES=cron

WORKDIR /usr/src/app
ENTRYPOINT ["/entrypoint.sh"]
CMD cron -f

RUN apt-get update \
    && apt-get -y --no-install-recommends install ${PACKAGES} \
    && touch /var/log/cron.log \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /
COPY crontab /tmp/crontab
RUN cat /tmp/crontab | crontab -

COPY . /usr/src/app/

RUN pip3 install -r requirements.txt
