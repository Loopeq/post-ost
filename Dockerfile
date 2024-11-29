FROM python:3.10.12 as requirements-stage

WORKDIR /tmp

COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /code/src

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
