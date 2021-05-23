#Tells Docker to use the official python 3 image from dockerhub as a base image
FROM python:3

# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Sets the container's working directory to /app
WORKDIR /app

EXPOSE 8000

# sets the environment variable
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=ouveai.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

# Copies all files from our local project into the container
COPY ./src /app
COPY ./requirements.txt /app/

# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r requirements.txt

# Install assets
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/static

# Run application
CMD gunicorn ouveai.wsgi:application