import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'features.todos',
)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'todos-tests',
            'USER': 'grpc-demo-user',
            'PASSWORD': 'grpc-demo-project-pass',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# CHANGE THE SECRET KEY IN YOUR CODE
SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjoxNjM5NDQ3ODA2fQ'