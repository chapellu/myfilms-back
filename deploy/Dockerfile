FROM python:3.11-slim

WORKDIR /opt/myfilms

RUN apt-get update

COPY myfilms /opt/myfilms/myfilms
COPY pyproject.toml /opt/myfilms
COPY README.md /opt/myfilms/


# Configure Poetry
ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN poetry install --only main --no-interaction --no-cache

# Run Application
EXPOSE 8000
CMD [ "poetry", "run", "dev" ]
