from django.db import models
from datetime import datetime
from doctors.models import Doctor
from hospitals.models import Hospital
from accounts.models import User
# Create your models here.
class DocReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user
class HosReview(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user