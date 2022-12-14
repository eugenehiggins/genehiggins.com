# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9-alpine3.13
LABEL maintainer="genehiggins.com"

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

COPY ./genehigginswebsite/requirements.txt /tmp/requirements.txt
COPY ./genehigginswebsite/requirements.dev.txt /tmp/requirements.dev.txt
COPY ./genehigginswebsite /genehigginswebsite

# Use /app folder as a directory where the source code is stored.
WORKDIR /genehigginswebsite

# Port used by this container to serve HTTP.
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
      build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        wagtail-user

ENV PATH="/py/bin:$PATH"

USER wagtail-user
#
#
## Install system packages required by Wagtail and Django.
#RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
#    build-essential \
#    libpq-dev \
#    libmariadbclient-dev \
#    libjpeg62-turbo-dev \
#    zlib1g-dev \
#    libwebp-dev \
# && rm -rf /var/lib/apt/lists/*
#
## Install the application server.
#RUN pip install "gunicorn==20.0.4"
#
## Install the project requirements.
#RUN pip install -r /requirements.txt
#
#
## Set this directory to be owned by the "wagtail" user. This Wagtail project
## uses SQLite, the folder needs to be owned by the user that
## will be writing to the database file.
#RUN chown wagtail:wagtail /app
#
## Copy the source code of the project into the container.
#COPY --chown=wagtail:wagtail . .
#
## Use user "wagtail" to run the build commands below and the server itself.
#USER wagtail
#
## Collect static files.
#RUN python manage.py collectstatic --noinput --clear
#
## Runtime command that executes when "docker run" is called, it does the
## following:
##   1. Migrate the database.
##   2. Start the application server.
## WARNING:
##   Migrating database at the same time as starting the server IS NOT THE BEST
##   PRACTICE. The database should be migrated manually or using the release
##   phase facilities of your hosting platform. This is used only so the
##   Wagtail instance can be started with a simple "docker run" command.
#CMD set -xe; python manage.py migrate --noinput; gunicorn genehigginswebsite.wsgi:application
