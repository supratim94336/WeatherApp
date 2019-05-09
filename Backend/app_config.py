import os

basedir = os.path.abspath(os.path.dirname(__file__))

# you can always hide the secret key with environment variables
DARKSKY_API = os.environ.get('DARKSKY_API')
CERTIFICATE = os.environ.get('CERTIFICATE')