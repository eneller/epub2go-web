FROM python:3.12
VOLUME [ "/app/src/epub2go_web/media" ]
EXPOSE 50000/tcp
EXPOSE 50000/udp
ENV DJANGO_DEBUG=FALSE
ARG BUILDARCH


WORKDIR /app
# Install dependencies
# Manually install pandoc because debian repo version is ooold
RUN <<EOF
wget -O pandoc.deb https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-1-${BUILDARCH}.deb \
&& dpkg -i pandoc.deb
EOF

COPY --from=ghcr.io/astral-sh/uv:0.7.18 /uv /uvx /bin/
# Install python deps
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Copy the project into the image
ADD . /app

WORKDIR /app/src
CMD ["uv", "run", "gunicorn", "-c", "gunicorn.py"]
