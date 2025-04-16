from django.contrib import admin
from .models import UserResponse,ContactSubmission # import your model

admin.site.register(UserResponse)
admin.site.register(ContactSubmission)