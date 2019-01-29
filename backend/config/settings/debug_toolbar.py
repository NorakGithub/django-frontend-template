import socket
import environ

env = environ.Env()

if env.bool('DJANGO_DEBUG', True):
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']
else:
    INTERNAL_IPS = env.list('DJANGO_INTERNAL_IPS')
