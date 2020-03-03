import os


def http_port():
  p = os.getenv('HTTP_PORT', '8000')
  return int(p)


def http_host():
  p = os.getenv('HTTP_HOST', '0.0.0.0')
  return str(p)


def log_level():
  l = os.getenv('LOG_LEVEL', 'INFO')
  return str(l)


def log_debug():
  d = os.getenv('DEBUG', False)
  return bool(d)
