import environ

ROOT_DIR = environ.Path(__file__) - 3
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = str(ROOT_DIR.path('static'))
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = str(ROOT_DIR.path('media'))
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    str(ROOT_DIR.path('static_files')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
