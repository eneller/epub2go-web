FROM python:3.12
VOLUME [ "/app/src/epub2go_web/media" ]
EXPOSE 50000/tcp
EXPOSE 50000/udp

COPY --from=ghcr.io/astral-sh/uv:0.7.18 /uv /uvx /bin/

WORKDIR /app
# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Copy the project into the image
ADD . /app

WORKDIR /app/src
CMD ["uv", "run", "gunicorn", "-c", "gunicorn.py"]