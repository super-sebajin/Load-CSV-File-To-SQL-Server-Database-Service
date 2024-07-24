# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.10.6
FROM python:${PYTHON_VERSION}-slim as base
# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv
 
WORKDIR /load-data-file-service
COPY . .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl gnupg

# Add Microsoft repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

RUN apt-get install -y unixodbc-dev
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17

# Activate the virtual environment
RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


#insert perl execute command around here, so that the container

# Run the application.
CMD uvicorn app.api.api_app:app --host=0.0.0.0 --port=8000 --reload