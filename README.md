# epub2go-web
A simple Website to provide a `NNI (Non-Nerd Interface)` to [epub2go.py](https://github.com/eneller/epub2go.py), a web to epub converter.

## Development
This project uses [watchman](https://facebook.github.io/watchman/) for file watching and reloading.
Follow the [official instructions](https://facebook.github.io/watchman/docs/install.html) for your system to install, django will default to its standard watcher otherwise.

To run the server, install the dependencies described in `pyproject.toml` and `uv.lock`
in a virtual environment, ideally using [uv](https://docs.astral.sh/uv/) (or pip).

[Celery](https://docs.celeryq.dev/en/stable/) is used as a task queue with [redis](https://hub.docker.com/_/redis) as backend.
A container for it is provided in the `src/docker-compose.yml`.
After the container is up, simply start your Celery workers from `src/` using
```bash
celery -A epub2go_web worker --loglevel=INFO
```

Finally, run the **development** server using
```bash
python manage.py runserver
```

## Deployment
[Gunicorn](https://gunicorn.org/) does not serve static files and is intended to be deployed behind [nginx](https://nginx.org/).
An example configuration is provided in `nginx.conf`.

To collect the static files for nginx, run
```bash
python manage.py collectstatic
```
and point nginx to the resulting folder.

### Docker
Run the `docker-compose.yml` in the project root using
```bash
docker compose up
```
### Manual
Follow the Development instructions, except replace the final command for the development server with
```bash
gunicorn -c gunicorn.py
```
