# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.10.6
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv
 
WORKDIR /trigger-etl-data-upload-service
COPY . .

RUN apt-get update && apt-get upgrade -y

# RUN apt-get install perl-modules -y

# Activate the virtual environment
RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application.

# COPY ./app ./app

# ENTRYPOINT [ "uvicorn", "app.api.api_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD uvicorn app.api.api_app:app --host=0.0.0.0 --port=8000 --reload