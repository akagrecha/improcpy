# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fxx1q83tamoh5*+_9-u#!g)q%$hk16w=k7=6&zaq_-h8fncqbq'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Email server settings
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 25

EMAIL_HOST_USER = ""

EMAIL_HOST_PASSWORD = ""

# Email Id which will appear in From header in email
EMAIL_FROM = ""

SERVER_EMAIL = ""

EMAIL_SUBJECT_PREFIX = '[improcpyWeb] '

ADMINS = (
    ('Ranveer Aggarwal', 'ranveeraggarwal@gmail.com'),
    ('Anmol Kagrecha', 'akagrecha@gmail.com'),
)

MEDIA_URL = "/media/"

STATIC_URL = "/static/"

MEDIA_NGINX_REDIRECT = "/media/uploads/"

SESSION_COOKIE_PATH = "/"

CSRF_COOKIE_PATH = "/"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')