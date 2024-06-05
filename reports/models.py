from django.db import models
from accounts.models import Profile
import uuid

class Report(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('correction', 'correction'),
        ('approve', 'approve'),
        ('reject', 'reject')
    )

    account_owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, db_index=True)
    description = models.TextField(null=True, blank=True, db_index=True)
    main_category = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    sub_category = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    status = models.CharField(max_length=255, default="pending", null=True, blank=True, choices=STATUS, db_index=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_index=True)
    updated_time_stamp = models.DateTimeField(auto_now=True, db_index=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display REPORTS by usernames in the database
    def __str__(self):
        return self.account_owner.username

    # display new invoice first
    class Meta:
        ordering = ['-created_time_stamp']
    
    


