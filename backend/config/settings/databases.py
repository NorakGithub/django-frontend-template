import environ

env = environ.Env()
# Database configuration
DEFAULT_DB_URL = "postgres://postgres:postgres@localhost:5432/hero_amw"
DATABASES = {'default': env.db("DATABASE_URL", default=DEFAULT_DB_URL)}
DATABASES['default']['ATOMIC_REQUESTS'] = True
