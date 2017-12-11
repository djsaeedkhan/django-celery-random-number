import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_number(total):
    for i in range(total):
        total=get_random_string(8)
    return "Random Number Created..."