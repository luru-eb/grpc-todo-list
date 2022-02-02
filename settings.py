import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'models',
)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'todos'),
            'USER': os.getenv('DB_USER', 'postgres'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'mysecretpassword'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# CHANGE THE SECRET KEY IN YOUR CODE
SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjoxNjM5NDQ3ODA2fQ'
