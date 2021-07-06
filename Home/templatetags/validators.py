import os

from django.contrib import messages
from django.http import request


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        messages.error(request, 'Unsupported file or Corrupted image. ')
