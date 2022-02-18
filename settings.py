import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'features.todos',
)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'todos'),
            'USER': os.getenv('DB_USER', 'grpc-demo-user'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'grpc-demo-project-pass'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# CHANGE THE SECRET KEY IN YOUR CODE
SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjoxNjM5NDQ3ODA2fQ'
