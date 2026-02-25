from django.utils.crypto import get_random_string
from .models import URLSTORAGE


def generate_random_code(length=8):
    while True:
        code = get_random_string(length)
        if not URLSTORAGE.objects.filter(short_code= code).exists():
            return code 