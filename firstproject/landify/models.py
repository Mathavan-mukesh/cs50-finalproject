from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class UserResponse(models.Model):
    STATE_CHOICES = [
        ('KA', 'Karnataka'),
        ('MH', 'Maharashtra'),
        ('DL', 'Delhi'),
        ('TN', 'Tamil Nadu'),
        ('GJ', 'Gujarat'),
    ]

    location_text = models.CharField(max_length=255) 
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    district = models.CharField(max_length=100)  
    pincode = models.PositiveIntegerField(
        validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999)
        ]
    )
    rate = models.IntegerField() 
    way = models.BooleanField()  
    picture = models.ImageField(upload_to='pictures/')
    phone_number = models.CharField(max_length=15, blank=True)
    area = models.CharField(max_length=15, blank=True)
    
    

    def __str__(self):
        return f"{self.location_text}, {self.get_state_display()}, {self.district}"


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"