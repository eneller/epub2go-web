# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "epub2go_web.wsgi"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 4
# The socket to bind
bind = "0.0.0.0:50000"
# Restart workers when code changes (development only!)
#reload = True
# Write access and error info to /var/log
#accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
#pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
#daemon = True
