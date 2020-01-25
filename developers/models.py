from django.db import models
from django.contrib.auth.models import User

class Developer(User):
    """
    Developer model. Another kind User. 
    """
    developer_id = models.AutoField(primary_key=True)
    #user = models.OneToOneField(User, default=None, on_delete=models.CASCADE) 